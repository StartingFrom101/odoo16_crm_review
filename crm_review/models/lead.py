from odoo import models, fields

class Lead(models.Model):
    _name = "lead"
    _description = "CRM Leads"

    name = fields.Char(required=True,  )
    description = fields.Char()
    contact_id = fields.Many2one('res.partner', required=True)
    
    # Tasks
    task_ids = fields.One2many('lead.task', 'lead_id')
    
    # Opportunity
    opportunity_ids = fields.One2many('lead.opportunity', 'lead_id') 
    