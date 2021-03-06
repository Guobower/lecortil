from openerp import models, fields, api

class sale_order_line_eater(models.Model):
    _inherit = 'sale.order.line'

    eater = fields.Many2one('cortil.eater', string="Consommateur")
    
    def onchange_eater(self, cr, uid, ids, eater, context=None):
        sol = self.pool.get('sale.order.line').browse(cr, uid, ids, context=context)
        if sol.eater and sol.eater.id:
            self.pool.get('cortil.eater').write(cr, uid, eater, {'partner': sol.order_id.partner_id.id})
