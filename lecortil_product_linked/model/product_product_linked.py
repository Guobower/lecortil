from openerp import models, fields, api

class product_product_linked(models.Model):
    _name = 'product.product.linked'

    child_product = fields.Many2one('product.product', string="Produits liées")
    quantity = fields.Integer(string='Quantité')