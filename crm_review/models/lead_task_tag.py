from odoo import models, fields

class LeadTaskTags(models.Model):
    _name = 'lead.task.tag'
    _description = 'Lead Task Tags'
    
    color = fields.Integer()
    name = fields.Char(required=True)