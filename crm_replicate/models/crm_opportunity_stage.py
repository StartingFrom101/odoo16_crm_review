from odoo import models, fields, api

class CrmOpportunityStage(models.Model):
    _name = 'crm.opportunity.stage'
    _description = 'Crm Opportunity Stage'
    _order = 'sequence' 
       
    name = fields.Char()
    fold = fields.Boolean(default = False)
    sequence = fields.Integer(default = 1)
    active = fields.Boolean(default = True)
    
    