from openerp import models, fields, api

class cortil_tour(models.Model):
    _name = 'cortil.tour'

    name = fields.Char(string='Nom')
    description = fields.Char(string='Description HTML')