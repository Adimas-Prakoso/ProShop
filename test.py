import json
import random
import logging

def get_10_raandom_discount_items():
    try:
        # Read existing product data from file
        with open('./database/admin/item/items.json', 'r') as file:
            products = json.load(file)

        # Filter products by discount
        discounted_products = [product for product in products if product['discount'] > 0]

        # Get 10 random items with discount
        random_discount_items = random.sample(discounted_products, 10)

        return random_discount_items
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

if __name__ == '__main__':
    items = get_10_raandom_discount_items()[0]["id"]
    print(items)