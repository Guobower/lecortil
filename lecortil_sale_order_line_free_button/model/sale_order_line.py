from openerp import models, fields

class sale_order_line_free(models.Model):
    _inherit = 'sale.order.line'

    free = fields.Boolean(string='Gratuit',default=False)

    def set_free(self,cr,uid,ids,context=None):
        sol = self.pool.get('sale.order.line').browse(cr, uid, ids, context=context)
        if sol.free:
            sol.free = False
        else:
            sol.free = True 