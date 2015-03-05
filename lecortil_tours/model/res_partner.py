from openerp import models, fields, api

class res_partner_eater(models.Model):
    _inherit = 'res.partner'

    tour = fields.Many2one('cortil.tour', string="Tournée", index=True)