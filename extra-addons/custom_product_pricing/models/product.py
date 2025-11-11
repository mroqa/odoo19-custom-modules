from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    profit_margin = fields.Float(string='Profit Margin (%)', default=20.0)
    auto_price = fields.Float(string='Auto Calculated Price', compute='_compute_auto_price')

    @api.depends('standard_price', 'profit_margin')
    def _compute_auto_price(self):
        for product in self:
            if product.standard_price:
                product.auto_price = product.standard_price * (1 + product.profit_margin / 100)
            else:
                product.auto_price = 0.0
