from odoo import fields, models

class LeadOpportunityStage(models.Model):
    _name = 'lead.opportunity.stage'
    _description = 'Lead Opportunity Stage'

    name = fields.Char()
    sequence = fields.Integer(default='1')
    