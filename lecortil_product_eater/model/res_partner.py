from openerp import models, fields, api

class res_partner_eater(models.Model):
    _inherit = 'res.partner'

    eaters = fields.One2many('cortil.eater','partner', string="Consommateurs", index=True)