from odoo import api, fields, models

class LeadOpportunity(models.Model):
    _name = 'lead.opportunity'
    _description = 'Lead Opportunity'
    
    lead_id = fields.Many2one('crm.lead', string="Lead")
    name = fields.Char()
    description = fields.Char()
    stage = fields.Selection(
        [('qualification', 'Qualification'), ('assessment', 'Assessment'), ('proposal', 'Proposal'), ('negotiation', 'Negotiation'), ('won', 'Won'), ('lost', 'Lost')],
    )
    
    close_date = fields.Date()
    responsible_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
    value = fields.Float()
    
    