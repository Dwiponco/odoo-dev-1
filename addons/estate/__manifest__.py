{
    'name': 'Real Estate',
    'version': '1.0.0',
    'summary': 'Real Estate',
    'description': 'Real Estate',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'data': [
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',
        'security/ir.model.access.csv',
    ]
}