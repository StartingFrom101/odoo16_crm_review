from odoo import api, models, fields
from odoo.exceptions import ValidationError
class LeadTask(models.Model):
    _name = 'lead.task'
    _description = 'Lead Task'
    _sql_constraints = [
    ]
    _order = 'due_date desc'
    
    
    lead_id = fields.Many2one('lead', string="Lead")
    name = fields.Char(required=True)
    description = fields.Text()
    
    # Tags type
    tag_ids = fields.Many2many('lead.task.tag', string="Tags")
    
    # Task creator
    user_id = fields.Many2one('res.users', string='Creator', default=lambda self: self.env.user)
    
    due_date = fields.Date(required=True, default=fields.Date.add(fields.Date.today(), days=3))
    
    finished_date = fields.Date(readonly=True)
    state = fields.Selection([('open', 'Open'), ('finished', 'Finished')], default='open', readonly=True) 
    
    def finish_task(self):
        for record in self:
            record.state = 'finished'
            record.finished_date = fields.Date.today()
        
    @api.constrains('due_date')
    def _check_due_date(self):
        for record in self:
            if record.due_date < fields.Date.today():
                raise ValidationError('Due date cannot be in the past!') 

