# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Openacademy',
    'author': 'Daniel',
    'version': '1.0',
    'category': 'Sales',
    'sequence': 15,
    'summary': 'Course and session',
    'description': """
        Modulos para crear cursos y sesiones academicas
    """,
    'website': 'https://www.soluziono.com',
    'depends': ['base'],
    'data': ['views/course_view.xml', 'views/partner_view.xml', 'wizard/create_attendee_view.xml'],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
