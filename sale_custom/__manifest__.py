# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale Custom',
    'version' : '1.0',
    'summary': 'Sale Custom for klaxindonesia',
    'sequence': 10,
    'category': 'Sale',
    'website': 'http://www.klaxindonesia.com',
    'depends': ['product', 'sale'],
    'data': [
        'views/sale_order.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
