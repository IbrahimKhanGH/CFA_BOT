from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

# Global storage for orders
orders = {}
last_ordered_item = {}

# Price list for menu items
price_list = {
    # Entrees
    "Chicken Sandwich": 4.29,
    "Deluxe Chicken Sandwich": 4.95,
    "Spicy Chicken Sandwich": 4.69,
    "Spicy Deluxe Sandwich": 5.25,
    "Grilled Chicken Sandwich": 5.65,
    "Grilled Chicken Club Sandwich": 7.25,
    "Nuggets (8-count)": 4.05,
    "Nuggets (12-count)": 5.95,
    "Grilled Nuggets (8-count)": 5.25,
    "Grilled Nuggets (12-count)": 7.85,
    "Chick-n-Strips (3-count)": 4.35,
    "Chick-n-Strips (4-count)": 5.19,
    "Chick-fil-A Cool Wrap": 6.75,
    "Grilled Cool Wrap": 6.79,

    # Salads
    "Cobb Salad": 8.19,
    "Spicy Southwest Salad": 8.19,
    "Market Salad": 8.19,
    "Side Salad": 4.09,

    # Sides
    "Waffle Potato Fries (Small)": 1.89,
    "Waffle Potato Fries (Medium)": 2.15,
    "Waffle Potato Fries (Large)": 2.45,
    "Mac & Cheese (Small)": 2.99,
    "Mac & Cheese (Medium)": 3.55,
    "Mac & Cheese (Large)": 5.25,
    "Fruit Cup (Small)": 2.85,
    "Fruit Cup (Medium)": 3.25,
    "Fruit Cup (Large)": 4.25,
    "Chicken Noodle Soup (Small)": 2.65,
    "Chicken Noodle Soup (Large)": 4.65,
    "Greek Yogurt Parfait": 3.45,
    "Side of Kale Crunch": 1.85,
    "Waffle Potato Chips": 1.89,

    # Beverages
    "Freshly-Brewed Iced Tea Sweetened (Small)": 1.65,
    "Freshly-Brewed Iced Tea Sweetened (Medium)": 1.85,
    "Freshly-Brewed Iced Tea Sweetened (Large)": 2.15,
    "Freshly-Brewed Iced Tea Unsweetened (Small)": 1.65,
    "Freshly-Brewed Iced Tea Unsweetened (Medium)": 1.85,
    "Freshly-Brewed Iced Tea Unsweetened (Large)": 2.15,
    "Chick-fil-A Lemonade (Small)": 1.99,
    "Chick-fil-A Lemonade (Medium)": 2.29,
    "Chick-fil-A Lemonade (Large)": 2.69,
    "Chick-fil-A Diet Lemonade (Small)": 1.99,
    "Chick-fil-A Diet Lemonade (Medium)": 2.29,
    "Chick-fil-A Diet Lemonade (Large)": 2.69,
    "Soft Drink (Small)": 1.65,
    "Soft Drink (Medium)": 1.85,
    "Soft Drink (Large)": 2.15,
    "1% Chocolate Milk": 1.29,
    "1% White Milk": 1.29,
    "Simply Orange Juice": 2.25,
    "Bottled Water": 1.79,
    "Coffee": 1.65,
    "Iced Coffee (Small)": 2.69,
    "Iced Coffee (Large)": 3.09,
    "Sunjoy (Small)": 1.99,
    "Sunjoy (Medium)": 2.29,
    "Sunjoy (Large)": 2.69,

    # Treats
    "Frosted Lemonade (Small)": 3.85,
    "Frosted Lemonade (Large)": 4.45,
    "Frosted Coffee (Small)": 3.85,
    "Frosted Coffee (Large)": 4.45,
    "Milkshake (Small)": 3.45,
    "Milkshake (Large)": 4.25,
    "Peppermint Chocolate Chip Milkshake (Small)": 3.65,
    "Peppermint Chocolate Chip Milkshake (Large)": 4.45,
    "Chocolate Chunk Cookie": 1.29,
    "Chocolate Chunk Cookie (6-count)": 7.29,
    "Icedream Cone": 1.39,
    "Icedream Cup": 1.25,
    "Chocolate Fudge Brownie": 1.89,

    # Kid's Meals
    "Nuggets Kid's Meal (4-count)": 3.35,
    "Nuggets Kid's Meal (6-count)": 4.05,
    "Grilled Nuggets Kid's Meal (4-count)": 3.75,
    "Grilled Nuggets Kid's Meal (6-count)": 4.45,
    "Chick-n-Strips Kid's Meal (1-count)": 3.25,
    "Chick-n-Strips Kid's Meal (2-count)": 3.95,

    # Breakfast Items
    "Chick-fil-A Chicken Biscuit": 3.09,
    "Spicy Chicken Biscuit": 3.29,
    "Chick-n-Minis (4-count)": 4.49,
    "Egg White Grill": 4.35,
    "Hash Brown Scramble Burrito": 3.75,
    "Hash Brown Scramble Bowl": 4.65,
    "Sausage Biscuit": 2.19,
    "Bacon, Egg & Cheese Biscuit": 3.59,
    "Sausage, Egg & Cheese Biscuit": 3.79,
    "Chicken, Egg & Cheese Bagel": 4.79,
    "Hash Browns": 1.09,
    "Greek Yogurt Parfait (Breakfast)": 3.45,
    "Fruit Cup (Breakfast, Small)": 2.85,

    # Sauces and Dressings (if applicable)
    "Chick-fil-A Sauce": 0.00,
    "Polynesian Sauce": 0.00,
    "Garden Herb Ranch Sauce": 0.00,
    "Zesty Buffalo Sauce": 0.00,
    "Honey Mustard Sauce": 0.00,
    "Barbeque Sauce": 0.00,
    "Sweet and Spicy Sriracha Sauce": 0.00,
    "Honey Roasted BBQ Sauce": 0.00,

    # Dressings
    "Avocado Lime Ranch Dressing": 0.00,
    "Fat-Free Honey Mustard Dressing": 0.00,
    "Garden Herb Ranch Dressing": 0.00,
    "Light Balsamic Vinaigrette Dressing": 0.00,
    "Light Italian Dressing": 0.00,
    "Zesty Apple Cider Vinaigrette Dressing": 0.00,
}

# Item name mapping and size required items
item_name_mapping = {
    "Waffle Fries": "Waffle Potato Fries",
    "Milkshake": "Milkshake",
    # Add other mappings as needed
}

size_required_items = [
    "Waffle Potato Fries",
    "Mac & Cheese",
    "Fruit Cup",
    "Chicken Noodle Soup",
    "Freshly-Brewed Iced Tea Sweetened",
    "Freshly-Brewed Iced Tea Unsweetened",
    "Chick-fil-A Lemonade",
    "Chick-fil-A Diet Lemonade",
    "Soft Drink",
    "Iced Coffee",
    "Sunjoy",
    "Frosted Lemonade",
    "Frosted Coffee",
    "Milkshake",
    "Peppermint Chocolate Chip Milkshake"
]

# Add this function at the top with your other helper functions


def calculate_total(order_items):
    total = 0
    for item in order_items:
        food_item = item['food_item']
        quantity = item.get('quantity', 1)
        # Get base price from price list
        price = price_list.get(food_item, 0)
        total += price * quantity
    return total


# Add this mapping for items that need prefixes
item_prefix_mapping = {
    "Cool Wrap": "Grilled Cool Wrap",
    # Add other items that need prefixes
}

# Add this helper function


def create_response(message):
    return jsonify({
        'fulfillmentText': message,
        'fulfillmentMessages': [
            {
                'text': {
                    'text': [message]
                }
            }
        ]
    })


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        print("\n=== WEBHOOK REQUEST ===")
        req = request.get_json(silent=True, force=True)

        # Detailed debug logging
        query_result = req.get('queryResult', {})
        intent = query_result.get('intent', {})

        print("Intent Data:", {
            'displayName': intent.get('displayName'),
            'parameters': query_result.get('parameters'),
            'queryText': query_result.get('queryText'),
            'fulfillmentText': query_result.get('fulfillmentText')
        })

        # Check if intent names match exactly
        intent_name = intent.get('displayName')
        print(f"Received intent: '{intent_name}'")
        print(f"Intent type: {type(intent_name)}")  # Check if it's a string

        if req is None:
            return jsonify({'fulfillmentText': "Invalid request format."})

        print("Raw Request:", json.dumps(req, indent=2))

        session_id = req.get('session')
        query_result = req.get('queryResult', {})
        intent_name = query_result.get('intent', {}).get('displayName')
        query_text = query_result.get('queryText', '').lower()
        parameters = query_result.get('parameters', {})

        # Initialize orders if needed
        if session_id not in orders:
            orders[session_id] = []

        print(f"Session ID: {session_id}")
        print(f"Received intent: {intent_name}")
        print(f"Query Text: {query_text}")
        print(f"Parameters: {parameters}")
        print(
            f"Current orders before processing: {orders.get(session_id, [])}")

        # Print out all your handled intents for comparison
        HANDLED_INTENTS = [
            'OrderFood',
            'OrderFood - size',
            'SpecifySize',
            'ModifyOrder',
            'SandwichSpicyOrNot',
            'SandwichSpicyOrNot - custom',
            'SandwichSpicyOrNot - custom-2',
            'ReviewOrder',
            'OrderCompletion',
            'ConfirmOrder',
            'Default Welcome Intent'
        ]
        print(
            f"Is intent '{intent_name}' in handled intents? {intent_name in HANDLED_INTENTS}")

        if intent_name == 'OrderFood':
            food_items = parameters.get('FoodItem', [])
            size = parameters.get('Size', '')

            for food_item in food_items:
                mapped_item = item_name_mapping.get(food_item, food_item)

                # If no size was specified for items that need size, ask for it
                if mapped_item in size_required_items and not size:
                    last_ordered_item[session_id] = {
                        'item': mapped_item,
                        'quantity': 1
                    }
                    return jsonify({
                        'fulfillmentText': f"What size would you like for your {food_item}? (Small, Medium, or Large)"
                    })

                # Add size if needed
                if mapped_item in size_required_items and size:
                    full_item_name = f"{mapped_item} ({size})"
                else:
                    full_item_name = mapped_item

                order_item = {
                    'food_item': full_item_name,
                    'quantity': 1
                }
                orders[session_id].append(order_item)
                print(f"Added to order: {order_item}")

                return create_response(f"1 {full_item_name} has been added to your cart. Would you like anything else?")

        elif intent_name == 'OrderFood - size':
            size = parameters.get('size', '')
            if session_id in last_ordered_item:
                pending_item = last_ordered_item[session_id]
                food_item = pending_item['item']
                quantity = pending_item['quantity']

                full_item_name = f"{food_item} ({size})"
                order_item = {
                    'food_item': full_item_name,
                    'quantity': quantity
                }
                orders[session_id].append(order_item)
                del last_ordered_item[session_id]

                return create_response(f"I've added {quantity} {full_item_name} to your order. Would you like anything else?")

        elif intent_name == 'SpecifySize':
            size = parameters.get('Size', '')
            if session_id in last_ordered_item:
                pending_item = last_ordered_item[session_id]
                food_item = pending_item['item']
                quantity = pending_item['quantity']

                full_item_name = f"{food_item} ({size})"
                order_item = {
                    'food_item': full_item_name,
                    'quantity': quantity
                }
                orders[session_id].append(order_item)
                del last_ordered_item[session_id]

                return create_response(f"I've added {quantity} {full_item_name} to your order. Would you like anything else?")

        elif intent_name == 'ModifyOrder':
            size = parameters.get('Size', '')

            # Check if this is a response to a size question for a new item
            if session_id in last_ordered_item:
                pending_item = last_ordered_item[session_id]
                food_item = pending_item['item']
                quantity = pending_item['quantity']

                mapped_item = item_name_mapping.get(food_item, food_item)
                full_item_name = f"{mapped_item} ({size})"

                order_item = {
                    'food_item': full_item_name,
                    'quantity': quantity
                }
                orders[session_id].append(order_item)
                del last_ordered_item[session_id]  # Clear the pending item

                return create_response(f"I've added {quantity} {full_item_name} to your order. Would you like anything else?")

        elif intent_name == 'SandwichSpicyOrNot':
            return create_response("Would you like your chicken sandwich original or spicy?")

        elif intent_name == 'SandwichSpicyOrNot - custom':
            order_item = {
                'food_item': 'Spicy Chicken Sandwich',
                'quantity': 1
            }
            orders[session_id].append(order_item)
            print(f"Added to order: {order_item}")
            return create_response("Sure, I have added a Spicy Chicken Sandwich to your order.")

        elif intent_name == 'SandwichSpicyOrNot - custom-2':
            order_item = {
                'food_item': 'Chicken Sandwich',
                'quantity': 1
            }
            orders[session_id].append(order_item)
            print(f"Added to order: {order_item}")
            return create_response("Sure, I have added a Chicken Sandwich to your order.")

        elif intent_name == 'ReviewOrder':
            order_items = orders.get(session_id, [])
            if not order_items:
                return jsonify({
                    'fulfillmentText': "You haven't ordered anything yet."
                })

            order_summary = ''
            for item in order_items:
                quantity = item.get('quantity', 1)
                food_item = item['food_item']
                order_summary += f"{quantity} x {food_item}\n"

            total_price = calculate_total(order_items)
            return create_response(f"Here's your current order:\n{order_summary}\nTotal: ${total_price:.2f}")

        elif intent_name == 'OrderCompletion':
            order_items = orders.get(session_id, [])
            if not order_items:
                return jsonify({
                    'fulfillmentText': "It seems you haven't ordered anything yet. What would you like to order?"
                })

            order_summary = ''
            for item in order_items:
                quantity = item.get('quantity', 1)
                food_item = item['food_item']
                price = price_list.get(food_item, 0)
                order_summary += f"{quantity} x {food_item} (${price:.2f} each)\n"

            total_price = calculate_total(order_items)
            return create_response(f"Thank you for your order! Here's what you ordered:\n{order_summary}\nTotal: ${total_price:.2f}\nWould you like to confirm your order?")

        elif intent_name == 'ConfirmOrder':
            # Handle order confirmation
            order_items = orders.get(session_id, [])
            if not order_items:
                return jsonify({
                    'fulfillmentText': "It seems you haven't ordered anything yet. What would you like to order?"
                })

            # Confirm the order
            order_summary = ''
            for item in order_items:
                quantity = item.get('quantity', 1)
                food_item = item['food_item']
                order_summary += f"{quantity} x {food_item}\n"

            total_price = calculate_total(order_items)
            # Clear the order after confirmation
            orders[session_id] = []
            return create_response(f"Your order has been confirmed! Here's what you ordered:\n{order_summary}\nTotal: ${total_price:.2f}\nThank you for choosing Chick-fil-A!")

        elif intent_name == 'Default Welcome Intent':
            return create_response("Welcome to Chick-fil-A! How can I help you today?")

        elif intent_name:  # If we have an intent name but didn't handle it
            print(f"WARNING: Unhandled intent: {intent_name}")
            return jsonify({
                'fulfillmentText': f"Debug: Received intent '{intent_name}' but no handler found."
            })
        else:
            print("WARNING: No intent name found in request")
            return jsonify({
                'fulfillmentText': "I'm sorry, I didn't understand that. Could you please rephrase?"
            })

        print(f"Current orders after processing: {orders.get(session_id, [])}")

    except Exception as e:
        print(f"Error in webhook: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'fulfillmentText': "I encountered an error processing your request."
        })


@app.route('/')
def index():
    return render_template('index.html')

# If you're using the Dialogflow API directly for your frontend, ensure you have the necessary setup.
# The following code is optional and only required if you're making direct API calls from your frontend.

# @app.route('/send_message', methods=['POST'])
# def send_message():
#     user_message = request.json.get('message')

#     # Send the message to Dialogflow
#     response = detect_intent_texts(
#         'your-project-id', 'unique-session-id', [user_message], 'en-US')

#     # Extract the reply
#     bot_reply = response.query_result.fulfillment_text
