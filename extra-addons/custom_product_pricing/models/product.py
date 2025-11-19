# models/product_template.py
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    profit_margin = fields.Float(string='Profit Margin (%)', default=20.0)
    auto_price = fields.Float(string='Auto Calculated Price', compute='_compute_auto_price', store=True, readonly=True)

    @api.depends('standard_price', 'profit_margin')
    def _compute_auto_price(self):
        for product in self:
            if product.standard_price:
                product.auto_price = product.standard_price * (1 + product.profit_margin / 100)
            else:
                product.auto_price = 0.0

    def action_apply_auto_price(self):
        """Copy auto price to Sales Price"""
        for product in self:
            product.list_price = product.auto_price
        return True