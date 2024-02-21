# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    image = fields.Image(related="product_id.image_1920")
    test = fields.Char(default="HIHIHI")

