from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Hospital Patient'
    
    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(readonly=True, string="Is Child?", tracking=True)
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], tracking = True)
    
    capitalized_name = fields.Char(string="Capitalized Name", compute="_compute_capitalized_name")
    
    ref = fields.Char(string="Reference", default=lambda self: "New")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    
    tag_ids = fields.Many2many('res.partner.category', 'hospital_patient_tag_rel', 'patient_id', 'tag_id' ,string="Tags")
    
    @api.model_create_multi 
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New'
        return super(HospitalPatient, self).create(vals_list)       
    
    @api.constrains('is_child', age)
    def _check_child_age(self):
        for record in self:
            if record.is_child and record.age < 18:
                raise ValidationError("Age cannot be less than 18 for a child")
    
    @api.depends('name')
    def _compute_capitalized_name(self):
        for record in self:
            if record.name:
                record.capitalized_name = record.name.upper()
            else:
                record.capitalized_name = ''
    
    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 18:
            self.is_child = True
        else:
            self.is_child = False 
            
            