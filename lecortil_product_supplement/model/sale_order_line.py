from openerp import models, fields, api

class sale_order_line_linked_products(models.Model):
    _inherit = 'sale.order.line'

    supplement_products_ids = fields.Many2many('product.product', string="Supplements")
    product_price_unit = fields.Float(string='Product Price',default=0.0)