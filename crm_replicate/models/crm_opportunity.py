from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, SUPERUSER_ID

class CrmOpportunity(models.Model):
    _name = 'crm.opportunity'
    _description = 'Crm Opportunity'
    _inherit = ['mail.thread']
    
    # Main Info
    name = fields.Char(string="Opportunity", required=True, tracking=True)
    revenue = fields.Float(required=True, tracking=True)
    probability = fields.Integer(required=True, tracking=True)
    # Customer Info
    partner_id = fields.Many2one('res.partner', string="Customer", tracking=True)
    email = fields.Char(string="Email", related='partner_id.email',readonly=False,  store=True, tracking=True)
    phone = fields.Char(string="Phone", related='partner_id.phone',readonly=False, store=True, tracking=True)
    # Sales info
    user_id = fields.Many2one('res.users', string="Salesperson", tracking=True, default = lambda self: self.env.user)
    expected_closing = fields.Date(string="Expected Closing", tracking=True)
    priority = fields.Selection([('0', 'Low'), ('1', 'Normal'), ('2', 'High'), ('3', 'Very High')], default='1', tracking=True)
    tag_ids = fields.Many2many('crm.opportunity.tag', string="Tags")
    deadline = fields.Char(string="Deadline", compute='_compute_deadline', store=True)
    # Stage
    stage_id = fields.Many2one('crm.opportunity.stage', group_expand='_read_group_stage_ids', string="Stage", tracking=True,)
    # Notes
    note = fields.Text(string="Notes")
    #Activities
    activity_ids = fields.One2many('crm.activity', 'opportunity_id', string='Activities', tracking=True,) 

    @api.depends('expected_closing')
    def _compute_deadline(self):
        for rec in self:
            if rec.expected_closing:
                today = fields.Date.today()
                delta = relativedelta(rec.expected_closing, today)
                rec.deadline = f"{delta.days} days"
                
    @api.model
    def _read_group_stage_ids(self, categories, domain, order):
        category_ids = categories._search([], order=order, access_rights_uid=SUPERUSER_ID)
        return categories.browse(category_ids)
