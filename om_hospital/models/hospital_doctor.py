from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = 'mail.thread'
    _description = 'Hospital Doctor'
    
    name = fields.Char(required = True, tracking = True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], tracking = True)
    ref = fields.Char(string="Reference", default=lambda self: "New")

    active = fields.Boolean(default=True, tracking=True)


    def name_get(self): 
        res = []
        for rec in self :
            name = f'{rec.ref} - {rec.name}'
            res.append((rec.id, name))
        return res 