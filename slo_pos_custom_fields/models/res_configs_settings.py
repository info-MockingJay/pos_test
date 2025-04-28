from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    receipt_logo = fields.Binary(string="Logo Image",
        related='pos_config_id.receipt_logo',readonly=False
    )

