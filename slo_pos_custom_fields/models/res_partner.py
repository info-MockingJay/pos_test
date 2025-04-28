from odoo import api, fields, models


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    date_of_birth = fields.Date('Date of Birth')

    @api.model
    def _load_pos_data_fields(self, config_id):
        result = super()._load_pos_data_fields(config_id)
        result.append('date_of_birth')


        print("load_pos_data_fields", result)
        return result

    def _load_pos_data(self, data):
        response = super()._load_pos_data(data)
        return response

