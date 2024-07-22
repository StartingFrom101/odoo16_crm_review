from odoo import fields, models


class CrmActivityType(models.Model):
    _name = 'crm.activity.type'
    _description = 'Crm Activity Type'
    
    name = fields.Char(string='Name')
    