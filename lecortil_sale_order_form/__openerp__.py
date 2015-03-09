{
    "name" : "Sale order form improvements",
    "version" : "1.0",
    "author" : "Bernard DELHEZ, AbAKUS it-solutions SARL",
    "category": 'Product',
    "description": """
This module removes some fields in the sale order in order to improve the easyness of use for workers.

It leaves for columns:
	- Product
	- Description
	- Supplements
	- Eater
	- Price
	- Subtotal
And adds:
	- The sum of products by category

It also removes all unecessary fields in the form head.

This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions, under the control of Valentin Thirion.
    """,
    'website': "http://www.abakusitsolutions.eu",
    'depends' : ['sale','lecortil_product_eater', 'lecortil_product_supplement',],
    'data': ['view/sale_order_view.xml',],
}
 
