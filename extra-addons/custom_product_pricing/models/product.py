from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    profit_margin = fields.Float(string='Profit Margin (%)', default=20.0)

    # Critical: store=True creates the database column
    auto_price = fields.Float(
        string='Auto Calculated Price',
        compute='_compute_auto_price',
        store=True,
        readonly=True
    )

    @api.depends('standard_price', 'profit_margin')
    def _compute_auto_price(self):
        for product in self:
            if product.standard_price:
                product.auto_price = product.standard_price * (1 + product.profit_margin / 100)
            else:
                product.auto_price = 0.0


    # @api.onchange('standard_price', 'profit_margin')
    # def _onchange_price_calculation(self):
    #     """Real-time price update in form view"""
    #     if self.standard_price:
    #         self.auto_price = self.standard_price * (1 + self.profit_margin / 100)
    #
    # @api.constrains('profit_margin')
    # def _check_profit_margin(self):
    #     """Validate profit margin is not negative"""
    #     for product in self:
    #         if product.profit_margin < 0:
    #             raise ValidationError("Profit margin cannot be negative!")
    #
    # def action_update_list_price(self):
    #     """Manual action to copy auto_price to sales price"""
    #     for product in self:
    #         product.list_price = product.auto_price
    #     return True
    #
