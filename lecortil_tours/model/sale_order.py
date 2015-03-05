from openerp import models, fields, api

class sale_order_line_linked_products(models.Model):
    _inherit = 'sale.order'

    tour = fields.Char(compute='_compute_tour_name',string="Tournée", store=False)
    
    @api.onchange('partner_id')
    def _compute_tour_name(self):
        self.tour = self.partner_id.tour.name