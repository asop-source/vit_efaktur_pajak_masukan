# -*- coding: utf-8 -*-
{
    'name': "vit e_fakture pajak masukan",

    'summary': """
        Perbaikan Form Vendor Bills
        """,


    'author': "asopkarawang@gmail.com",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'e_fakture',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','vit_efaktur','account','stock','vit_asset'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bills.xml',
    ],
}