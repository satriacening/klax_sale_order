# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    image = fields.Image(related="product_id.image_1920")
    price_subtotal_formatted = fields.Char(
        string="Subtotal",
        compute='_compute_amount_formatted',
        store=True, precompute=True)
    price_unit_formatted = fields.Char(
        string="Subtotal",
        compute='_compute_amount_formatted',
        store=True, precompute=True)
    product_uom_qty_formatted = fields.Char(compute='_compute_amount_formatted')

    price_after_disc = fields.Char(compute='_compute_amount_formatted')

    @api.depends('price_subtotal', 'price_unit')
    def _compute_amount_formatted(self):
        for record in self:
            record.price_subtotal_formatted = "{:,.0f}".format(record.price_subtotal or 0.0)
            record.price_unit_formatted = "{:,.0f}".format(record.price_unit or 0.0)
            record.product_uom_qty_formatted = "{:,.0f}".format(record.product_uom_qty or 0.0)
            after_discount = record.price_unit * (1 - record.discount / 100)
            record.price_after_disc = "{:,.0f}".format(after_discount or 0.0)
    test = fields.Char()

