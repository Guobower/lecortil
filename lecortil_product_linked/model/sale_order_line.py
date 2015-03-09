from openerp import models, fields, api

class sale_order_line_linked_products(models.Model):
    _inherit = 'sale.order.line'

    is_linked_products = fields.Boolean(string='Is linked products', default=False)