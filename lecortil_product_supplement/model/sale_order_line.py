from openerp import models, fields, api

class sale_order_line_linked_products(models.Model):
    _inherit = 'sale.order.line'

    supplement_products_ids = fields.Many2many('product.product', string="Suppléments")