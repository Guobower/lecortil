from openerp import models, fields, api

class cortil_eater(models.Model):
    _name = 'cortil.eater'

    name = fields.Char(string='Nom')
    partner = fields.Many2one('res.partner', string="Client", index=True)
