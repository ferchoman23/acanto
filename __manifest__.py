# -*- coding: utf-8 -*-
{
    'name': "Acanto",
    'summary': """
        Desarrollo para acanto""",
    'description': """
       Desarrollo para acanto
    """,
    'author': "ST",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['crm','base','account','infilefel'],
    'data': [
        #'views/crm_lead_views.xml',
        'views/account_move_views.xml',
        'security/security.xml',
        'report/report_contrasenia_pago.xml',
        'report/report_metodo_pago.xml',
        'views/report.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'aplication' : False,
}
