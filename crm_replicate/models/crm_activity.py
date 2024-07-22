from odoo import models, fields

class CrmActivity(models.Model):
    _name = 'crm.activity'
    _description = 'Crm Activity'

    opportunity_id = fields.Many2one('crm.opportunity', 'Opportunity',)
    type = fields.Many2one('crm.activity.type', string='Activity Type')
    due_date = fields.Date(string="Due on")
    summary = fields.Char()
    user_id = fields.Many2one('res.users', string='Assigned To', default = lambda self: self.env.user)
    