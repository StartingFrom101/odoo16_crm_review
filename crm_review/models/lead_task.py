from odoo import models, fields
class LeadTask(models.Model):
    _name = 'lead.task'
    _description = 'Lead Task'
    
    lead_id = fields.Many2one('lead', string="Lead")
    name = fields.Char(readonly=True)
    description = fields.Text()
    # Tags type
    tag_ids = fields.Many2many('lead.task.tag', string="Tags")
    # Task creator
    user_id = fields.Many2one('res.users', string='Creator', default=lambda self: self.env.user)
    due_date = fields.Date()
    finished_date = fields.Date(readonly=True)
    state = fields.Selection([('open', 'Open'), ('finished', 'Finished')], default='open') 