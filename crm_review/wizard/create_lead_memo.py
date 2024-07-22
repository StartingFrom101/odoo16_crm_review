from odoo import api, models, fields
class CreateMemoWizard(models.TransientModel):
    _name = 'create.lead.task.wizard'
    _description = 'Temporary Memo'
    
    name = fields.Char(string='Name', required=True, )
    
    