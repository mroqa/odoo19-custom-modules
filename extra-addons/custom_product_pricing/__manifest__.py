{
    'name': 'Auto Product Pricing',
    'version': '2.1',
    'author': "Mohammed Roqa",
    'category': 'Sales',
    'summary': 'Automatic price calculation based on profit margin',
    'description': """
        This module adds a 'Profit Margin (%)' field to the product template.
        It then automatically calculates the sales price based on the product's cost
        and the specified profit margin.
    """,
    'depends': ['base', 'product'],
    'data': ['views/product_template_views.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
