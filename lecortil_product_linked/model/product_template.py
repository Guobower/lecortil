from openerp import models, fields, api

class product_template_linked_products(models.Model):
    _inherit = 'product.template'

    required_linked_product_ids = fields.Many2many('product.product.linked', string="Produits liées")