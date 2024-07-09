from odoo import api, fields, models

class LeadOpportunity(models.Model):
    _name = 'lead.opportunity'
    _description = 'Lead Opportunity'
    
    lead_id = fields.Many2one('lead', string="Lead", required=True)
    name = fields.Char(required=True)
    description = fields.Char()
    
    stage_id = fields.Many2one('lead.opportunity.stage',)
    
    responsible_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
    close_date = fields.Date(readonly=True)
    value = fields.Float()
    