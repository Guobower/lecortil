{
    "name" : "Linked products management",
    "version" : "1.0",
    "author" : "Bernard DELHEZ, AbAKUS it-solutions SARL",
    "category": 'Product',
    "description": """
This module adds the possibility to link product and add linked to sale orders when clicking on the button in the SO.

This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions, under the control of Valentin Thirion.
    """,
    'website': "http://www.abakusitsolutions.eu",
    'depends' : ['sale',],
    'js' : ['static/src/js/add_linked_products.js',],
    'data': ['view/product_product_view.xml','view/sale_order_view.xml',],
}
 
