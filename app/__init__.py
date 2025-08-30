from flask import Flask

# Initialize the app
app = Flask(__name__)

# In-memory database for demonstration
# A list of dictionaries for products
PRODUCTS = [
    {'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 1200},
    {'id': 2, 'name': 'Smartphone', 'category': 'Electronics', 'price': 800},
    {'id': 3, 'name': 'Coffee Mug', 'category': 'Kitchenware', 'price': 15},
    {'id': 4, 'name': 'Running Shoes', 'category': 'Apparel', 'price': 100},
]

# A list of dictionaries for users
USERS = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
]

# Import routes after app initialization to avoid circular imports
from app import routes
