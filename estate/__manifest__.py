{
    'name': 'Estate',
    'depends': [
        'base',
                ],
    'category': 'Real Estate/Brokerage',
    'data': [
        
        
        'security/security.xml',
        'security/security_offer.xml',
        # 'security/ir.model.access.csv',
        # Security
        
        # Data
        
        # Wizard    
        "views/res_users_views.xml",    
        'views/estate_property_tag_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        # Views
        ],
    'application': True,
    'installable': True,
}