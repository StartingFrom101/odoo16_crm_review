{
    'name': 'Hospital Management System',
    'author': 'OpenERP',
    'website' : "https://www.odoo.com/",
    'summary': 'Hospital Management System',
    'description': "Hospital Management System",
    
    'version': '1.0',
    'category': 'Tools',
    'depends': ['base', 'mail'],
    
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/hospital_menu.xml'
    ],
    
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}