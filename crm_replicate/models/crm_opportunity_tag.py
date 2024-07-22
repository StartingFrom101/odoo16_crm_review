from odoo import models, fields

class CrmOpportunityTag(models.Model):
    _name = 'crm.opportunity.tag'
    _description = 'Crm Opportunity Tag'
    
    name = fields.Char()
    color = fields.Integer()