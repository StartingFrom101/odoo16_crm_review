from odoo import models, fields

class LeadTaskTags(models.Model):
    _name = 'lead.task.tag'
    _description = 'Lead Task Tags'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Tag name already exists!'),
    ]
    
    color = fields.Integer()
    name = fields.Char(required=True,)