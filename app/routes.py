from flask import render_template
from app import app, PRODUCTS

@app.route('/')
@app.route('/index')
def index():
    """Homepage route."""
    return render_template('index.html', title='Home', products=PRODUCTS)

@app.route('/product/<int:product_id>')
def product(product_id):
    """Product detail page route."""
    # Find the product by its ID
    product_item = next((p for p in PRODUCTS if p['id'] == product_id), None)

    if product_item:
        return render_template('product.html', title=product_item['name'], product=product_item)
    else:
        # A simple way to handle a product not being found
        return "Product not found", 404
