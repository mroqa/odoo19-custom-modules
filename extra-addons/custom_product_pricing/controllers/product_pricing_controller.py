# controllers/product_pricing_controller.py
from odoo import http
from odoo.http import request


class ProductPricingController(http.Controller):

    @http.route('/api/v1/product/<int:product_id>/auto_price',
                type='json', auth='user', methods=['POST'], csrf=False)
    def get_auto_price(self, product_id):
        # Fetch auto-calculated pricing for a product
        product = request.env['product.template'].browse(product_id)
        if not product.exists():
            return {'error': 'Product not found'}

        return {
            'product_id': product.id,
            'product_name': product.name,
            'standard_price': product.standard_price,
            'profit_margin': product.profit_margin,
            'auto_price': product.auto_price,
        }

    @http.route('/api/v1/product/update-margin', type='json', auth='user', methods=['POST'], csrf=False)
    def update_profit_margin(self, product_ids, new_margin):
        # Bulk update profit margins via API
        products = request.env['product.template'].browse(product_ids)
        products.write({'profit_margin': new_margin})
        return {'success': True, 'updated_count': len(products)}

