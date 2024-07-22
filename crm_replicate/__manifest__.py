{
    'name': 'Replicated CRM',
    'description': "Odoo 16 module study, CRM",
    'depends' : [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        
        'data/crm.opportunity.stage.csv',
        'data/crm.activity.type.csv',
        
        'views/crm_menu.xml',
        'views/crm_activity_views.xml',
        'views/crm_opportunity_views.xml'
    ],
    'installable': True,
    'application': True,
}