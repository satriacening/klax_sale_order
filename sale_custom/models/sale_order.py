# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order'

    @api.depends_context('lang')
    @api.depends('order_line.tax_id', 'order_line.price_unit', 'amount_total', 'amount_untaxed', 'currency_id')
    def _compute_tax_totals(self):
        for order in self:
            order_lines = order.order_line.filtered(lambda x: not x.display_type)
            order.tax_totals = self.env['account.tax']._prepare_tax_totals(
                [x._convert_to_tax_base_line_dict() for x in order_lines],
                order.currency_id or order.company_id.currency_id,
            )
            order.tax_totals['formatted_amount_total'] = self.remove_decimal_from_string(
                order.tax_totals['formatted_amount_total'])
            order.tax_totals['formatted_amount_untaxed'] = self.remove_decimal_from_string(
                order.tax_totals['formatted_amount_untaxed'])

            for group in order.tax_totals.get('groups_by_subtotal', {}).values():
                for line in group:
                    line['formatted_tax_group_amount'] = self.remove_decimal_from_string(
                        line['formatted_tax_group_amount'])
                    line['formatted_tax_group_base_amount'] = self.remove_decimal_from_string(
                        line['formatted_tax_group_base_amount'])
                    line['tax_group_name'] = '(PPn 11%)'
            for subtotal in order.tax_totals.get('subtotals', []):
                subtotal['formatted_amount'] = self.remove_decimal_from_string(subtotal['formatted_amount'])

    def remove_decimal_from_string(self, formatted_string):
        if formatted_string.endswith(".00"):
            return formatted_string[:-3]
        return formatted_string
