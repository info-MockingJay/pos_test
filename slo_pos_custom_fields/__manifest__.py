{
    'name': 'SLO POS Custom-Fields',
    'depends': ['base', 'web', 'point_of_sale'],
    'data': [
        'views/pos_res_config_settings_views.xml',
        'views/res_partner_views.xml',
    ],
    'assets': {'point_of_sale._assets_pos': [
        'slo_pos_custom_fields/static/src/**/*.js',
        'slo_pos_custom_fields/static/src/**/*.xml',
    ]},
    'author': 'Saw Lwin Oo',
    'version': '18.0',
    'license': 'LGPL-3',
}