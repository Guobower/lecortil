from openerp import models, fields, api

class sale_order_line_eater(models.Model):
    _inherit = 'sale.order.line'

    def print_sale_order_line(self,cr,uid,ids,context=None):
        return self.pool['report'].get_action(cr, uid, ids, 'sale.report_deliverieslabel', context=context)
