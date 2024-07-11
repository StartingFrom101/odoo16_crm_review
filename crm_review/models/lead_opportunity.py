from odoo import api, fields, models

class LeadOpportunity(models.Model):
    _name = 'lead.opportunity'
    _description = 'Lead Opportunity'
    _sql_constraints = [
        ('value_above_zero', 'CHECK(value > 0)', 'Value must be above zero!'),
        ('confidence_between_1_and_10', 'CHECK(confidence >= 1 and confidence <= 100)', 'Confidence must be between 1 and 100!')
    ]
    _order = 'value desc'
    
    lead_id = fields.Many2one('lead', string="Lead", required=True)
    name = fields.Char(required=True)
    description = fields.Char()
    
    stage_id = fields.Many2one('lead.opportunity.stage', string="Stage", required=True, default=lambda self: self.env['lead.opportunity.stage']._get_default_stage_id()) 
    stage_name = fields.Char(related='stage_id.name', readonly=True, string='Stage Name')

    responsible_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
    close_date = fields.Date(readonly=True)
    value = fields.Float(required=True)
    confidence = fields.Integer()
    
    estimated_value = fields.Float(compute='_compute_estimated_value', readonly=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([('open', 'Open'), ('closed', 'Closed')], default='open', readonly=True)
    
    

    def lost_opportunity(self):
        for opportunity in self:
            opportunity.close_date = fields.Date.today()
            opportunity.stage_id = opportunity.stage_id._get_lost_stage()
            # opportunity.active = False
            opportunity.state = 'closed'
            
    def won_opportunity(self):
        for opportunity in self:
            opportunity.close_date = fields.Date.today()
            opportunity.stage_id = opportunity.stage_id._get_won_stage()
            # opportunity.active = False
            opportunity.state = 'closed'
            
    def _get_default_stage_id(self):
        return self.stage_id._get_default_stage_id()
            
    @api.depends('value', 'confidence')
    def _compute_estimated_value(self):
        for opportunity in self:
            opportunity.estimated_value = opportunity.value * opportunity.confidence / 100
            
    def prospect_opportunity(self):
        for opportunity in self:
            opportunity.stage_id = opportunity.stage_id._get_prospect_stage()
            