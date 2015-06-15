Odoo (previously OpenERP) modules for sandwiches/food company
---
Odoo modules used for one of our customer who makes sandwiches.

Modules description 
---
- lecortil_labels_report : This module adds a new report on Sales Order that is used to be printed on labels for sandwiches/meals delivery. It is able to deal with 'tours' that are groups of customers being delivered by the same team (tours management is made with the module 'lecortil_tours'). This module also creates a paper_format for Odoo adapted to the real label dimensions.
- lecortil_sale_order_line_print : this module adds the Sales Order report as 'lecortil_labels_report' but accessible from each Sales Order Line with a button. The goal is to print one label at a time.
- lecortil_product_eater : This modules adds the possibility to save the 'subcustomer' information on each Sales Order Line. Each line represents one and only one meal for a person, so its name has to be set on the label. It also adds a way to save 'eaters' on customers. Theses eaters names will be printer in the reports labels in 'lecortil_tours'.
- lecortil_product_linked : This modules adds a way to link products to each other (product A with : B and C). This way, when you sell A, Odoo will auto add B and C to your Sales Order. This features is used to auto add bread when a soup is sold for example.
- lecortil_product_product_sol_name : This modules change the position of the product name and reference on the lines on sale order when a reference is set.
- lecortil_product_supplement : This module adds a supplement products management for sale order lines. Supplements are products that are added to one sale-order line in a one2many way. So you can have a product A (5$) that as for supplements B (1$) and C (1.5$) and the line price total will be 7.5$. The supplements will also be printed in the labels using the lecortil_labels_report module.
- lecortil_sale_order_form : This modules simply adapts the Sales Order form in order to match our customer need. The goal is to simplify the forms to improve the productivity by receiving order by phone.
- lecortil_sale_order_line_description : Add an empty description to a sale order line. It is used to add specific information that does not belong to the product itself.
- lecortil_sale_order_line_free_button : This module adds a set free or paying button in sale oder line. The result is that the line total price is simply set to zero.
- lecortil_tours : This modules adds a new model 'tours' to Odoo that contains some info. Tours are set for each customer and directly saved into Sales Order. The goal is to have a specific color selected on real-life labels for each tours.
---
These modules were developped by Bernard DELHEZ and Valentin THIRION for AbAKUS it-solutions SARL (http://www.abakusitsolutions.eu) in 2015.
---
