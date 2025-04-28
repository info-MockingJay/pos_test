from odoo import fields, models


class PosConfig(models.Model):

    _inherit = "pos.config"

    receipt_logo = fields.Binary(string="Logo Image")

