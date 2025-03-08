import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from recommendation import recommend_products




# Define the product database (mock data)
products = [
    {"id": 1, "name": "iPhone 13", "category": "Smartphone", "price": 799},
    {"id": 2, "name": "Samsung Galaxy S21", "category": "Smartphone", "price": 699},
    {"id": 3, "name": "MacBook Pro", "category": "Laptop", "price": 1299},
    {"id": 4, "name": "Sony WH-1000XM4", "category": "Headphones", "price": 350}
]

# Define a mock inventory
inventory = {
    "iPhone 13": 50,
    "Samsung Galaxy S21": 20,
    "MacBook Pro": 10,
    "Sony WH-1000XM4": 100
}

# Define the chatbot prompt template for product queries
product_prompt = PromptTemplate(
    input_variables=["product_query"],
    template="Customer is asking about product details. Respond as a helpful assistant. Query: {product_query}"
)

# Function to get product info using chatbot
def get_product_info(query):
    prompt = product_prompt.format(product_query=query)
    response = chat_openai.generate([prompt])
    return response['choices'][0]['text'].strip()

# Function to recommend products based on category
def recommend_products(category):
    recommended = [product for product in products if category.lower() in product['category'].lower()]
    return recommended

# Function for checkout process (mock)
def checkout_process(product_name, quantity):
    price = next((p['price'] for p in products if p['name'].lower() == product_name.lower()), None)
    
    if price:
        total_price = price * quantity
        return f"Your order for {quantity} x {product_name} has been placed. Total price: ${total_price}."
    else:
        return "Sorry, we couldn't find that product."

# Function to check inventory for a product
def check_inventory(product_name):
    stock = inventory.get(product_name, 0)
    if stock > 0:
        return f"{product_name} is in stock with {stock} units available."
    else:
        return f"Sorry, {product_name} is out of stock."

# Streamlit user interface
st.title("E-commerce AI Agent")

# Section 1: Chatbox to handle product queries
query = st.text_input("Ask a product-related question:")

if query:
    response = get_product_info(query)
    st.write("Chatbot Response:", response)

# Section 2: Product recommendations based on category
category = st.selectbox("Select a product category", ["Smartphone", "Laptop", "Headphones"])

if category:
    recommendations = recommend_products(category)
    st.write(f"Recommended products in {category} category:")
    for product in recommendations:
        st.write(f"{product['name']} - ${product['price']}")

# Section 3: Checkout process
product_name = st.text_input("Enter the product name for checkout:")
quantity = st.number_input("Enter quantity", min_value=1, step=1)

if st.button("Proceed to Checkout"):
    checkout_msg = checkout_process(product_name, quantity)
    st.write(checkout_msg)

# Section 4: Inventory check
inventory_check = st.text_input("Enter product name to check inventory:")

if inventory_check:
    inventory_status = check_inventory(inventory_check)
    st.write(inventory_status)
