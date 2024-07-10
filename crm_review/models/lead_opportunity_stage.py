from odoo import fields, models

class LeadOpportunityStage(models.Model):
    _name = 'lead.opportunity.stage'
    _description = 'Lead Opportunity Stage'

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Stage name already exists!'),
    ]

    name = fields.Char(required=True, readonly=True)
    sequence = fields.Integer(default='1')
    active = fields.Boolean(default=True)
    
    def name_get(self):
        return [(stage.id, stage.name) for stage in self]

    def _get_lost_stage(self):
        return self.search([('name', '=', 'Lost')], limit=1)
    
    def _get_won_stage(self):
        return self.search([('name', '=', 'Won')], limit=1)
    
    def _get_default_stage_id(self):
        return self.search([('name', '=', 'Assessment')], limit=1)
    
    def _get_prospect_stage(self):
        return self.search([('name', '=', 'Prospect')], limit=1)
    
    