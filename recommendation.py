from products import PRODUCTS



def recommend_products(category):
    # Simple recommendation based on category
    recommended = [product for product in PRODUCTS if product['category'] == category]
    return recommended