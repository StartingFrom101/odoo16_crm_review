# -*- coding: utf-8 -*-
{
    'name': "crm_review",

    'description': """
        Long description of module's purpose
    """,

    'installable': True,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        
        'views/crm_menus.xml',
        'views/lead_views.xml',
        'views/lead_task_views_1.xml',
        # 'views/lead_task_views.xml',
        'views/lead_opportunity_views.xml',
        # 'views/templates.xml',
        
        'data/lead.opportunity.stage.csv',
    ],
}
