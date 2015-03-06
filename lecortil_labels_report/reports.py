from openerp import models,api

class sale_order_delivery_labels(models.Model):
    _inherit = ['sale.order']

    def print_labels(self, cr, uid, ids, context=None):
        #report name: stock.report_deliverieslabels
        return self.pool['report'].get_action(cr, uid, ids, 'stock.report_deliverieslabels', context=context)
    


