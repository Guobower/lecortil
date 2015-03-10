from openerp import models, fields, api

class product_template_eater(models.Model):
    _inherit = 'product.template'

    category_name = fields.Char(related='categ_id.name', store=False)
