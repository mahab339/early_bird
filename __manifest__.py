# -*- coding: utf-8 -*-
{
    'name': "Early_bird",

    'summary': """Register and record attendance""",

    'description': """
        Early bird module for registering and recording attendance:
        - Register arrival.
        - Register leave.
        - Generate reports (for HR personnels only).
    """,

    'author': "Muhab Abdelreheem",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
