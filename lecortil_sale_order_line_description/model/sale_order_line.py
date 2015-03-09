from openerp import models, fields, api

class sale_order_line_linked_products_onchange(models.Model):
    _inherit = 'sale.order.line'
    
    description = fields.Char(string='Description')