# -*- coding: utf-8 -*-
{
    'name': "Rest api",

    'summary': """
       Curso de odoo_android esta vez es una prueba propia con el modulo de compras""",

    'description': """
       El objetivo seria obtener algunos datos de los pedidos de compra a traves de metodos HTTP 
    """,

    'author': "Osm soft",
    'website': "https://www.osm-soft.io/es",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','purchase'],
    'data': [
        'controllers/api.py',
    ],
}
