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

# Add this mapping dictionary at the top with your other global variables
item_name_mapping = {
    "Waffle Fries": "Waffle Potato Fries",
    "Milkshake": "Milkshake",
}

# Update or add the size_required_items list
size_required_items = [
    "Waffle Potato Fries",
    "Milkshake",
    # Add other items that require size
]

def calculate_total(order_items):
    total = 0.0
    for item in order_items:
        food_item = item['food_item']
        quantity = item.get('quantity', 1)
        # Calculate total price for each item
        total += price_list.get(food_item, 0) * quantity
    return total

def get_full_item_name(food_item, size):
    # First map the entity name to the price list name if needed
    mapped_item = item_name_mapping.get(food_item, food_item)
    
    # Items that require size specification
    size_required_items = [
        "Waffle Potato Fries",
        "Mac & Cheese",
        "Fruit Cup",
        "Chicken Noodle Soup",
        "Milkshake",
        "Freshly-Brewed Iced Tea Sweetened",
        "Freshly-Brewed Iced Tea Unsweetened",
        "Chick-fil-A Lemonade",
        "Chick-fil-A Diet Lemonade",
        "Soft Drink",
        "Iced Coffee",
        "Sunjoy",
        "Frosted Lemonade",
        "Frosted Coffee",
        "Peppermint Chocolate Chip Milkshake"
    ]

    # Check if the mapped item needs a size
    for item in size_required_items:
        if item in mapped_item:
            # If no size specified, default to Medium
            if not size:
                return f"{mapped_item} (Medium)"
            return f"{mapped_item} ({size})"
    
    return mapped_item

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        print("\n=== WEBHOOK REQUEST ===")
        req = request.get_json(silent=True, force=True)
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
        print(f"Current orders before processing: {orders.get(session_id, [])}")
        
        if intent_name == 'OrderFood':
            food_items = parameters.get('FoodItem', [])
            size = parameters.get('Size', '')
            
            # Fix quantity handling
            number_param = parameters.get('number', '')
            try:
                quantity = int(float(number_param)) if number_param else 1
            except (ValueError, TypeError):
                quantity = 1
            
            # Store the last ordered item and its quantity for size specification
            if food_items:
                last_ordered_item[session_id] = {
                    'item': food_items[0],
                    'quantity': quantity
                }
            
            for food_item in food_items:
                mapped_item = item_name_mapping.get(food_item, food_item)
                
                # If no size was specified for items that need size, ask for it
                if not size and mapped_item in size_required_items:
                    return jsonify({
                        'fulfillmentText': f"What size would you like for your {food_item}? (Small, Medium, or Large)"
                    })
                
                # Add size if needed
                if mapped_item in size_required_items:
                    full_item_name = f"{mapped_item} ({size or 'Medium'})"
                else:
                    full_item_name = mapped_item
                
                order_item = {
                    'food_item': full_item_name,
                    'quantity': quantity
                }
                orders[session_id].append(order_item)
                print(f"Added to order: {order_item}")
                
                return jsonify({
                    'fulfillmentText': f"{quantity} {full_item_name} has been added to your cart. Would you like anything else?"
                })

        elif intent_name == 'ModifyOrder':
            size = parameters.get('Size', '')
            
            # Check if this is a response to a size question for a new item
            if size and session_id in last_ordered_item:
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
                
                return jsonify({
                    'fulfillmentText': f"I've added {quantity} {full_item_name} to your order. Would you like anything else?"
                })
            
            # Regular size modification for existing items
            elif size and orders[session_id]:
                last_item = orders[session_id][-1]
                item_name = last_item['food_item']
                base_name = item_name.split(' (')[0]  # Remove existing size if present
                
                if base_name in size_required_items:
                    new_item_name = f"{base_name} ({size})"
                    orders[session_id][-1]['food_item'] = new_item_name
                    return jsonify({
                        'fulfillmentText': f"I've updated your {base_name} to {size} size. Anything else?"
                    })
                else:
                    return jsonify({
                        'fulfillmentText': f"Sorry, I can't modify the size of a {base_name}."
                    })
            
            # Handle spicy/original modifications
            if 'spicy' in query_text or 'original' in query_text:
                last_item = orders[session_id][-1]
                item_name = last_item['food_item']
                
                if 'Chicken Sandwich' in item_name:
                    if 'spicy' in query_text:
                        orders[session_id][-1]['food_item'] = 'Spicy Chicken Sandwich'
                        return jsonify({
                            'fulfillmentText': "I've changed your sandwich to Spicy Chicken Sandwich. Anything else?"
                        })
                    elif 'original' in query_text:
                        orders[session_id][-1]['food_item'] = 'Chicken Sandwich'
                        return jsonify({
                            'fulfillmentText': "I've changed your sandwich to Original Chicken Sandwich. Anything else?"
                        })
                
            # Default response if modification type not recognized
            return jsonify({
                'fulfillmentText': "I'm not sure how to modify your order that way. You can change sizes or switch between spicy and original for sandwiches."
            })

        elif intent_name == 'SandwichSpicyOrNot':
            return jsonify({
                'fulfillmentText': "Would you like your chicken sandwich original or spicy?"
            })

        elif intent_name == 'SandwichSpicyOrNot - custom':
            order_item = {
                'food_item': 'Spicy Chicken Sandwich',
                'quantity': 1
            }
            orders[session_id].append(order_item)
            print(f"Added to order: {order_item}")
            return jsonify({
                'fulfillmentText': f"Sure, I have added a Spicy Chicken Sandwich to your order."
            })

        elif intent_name == 'SandwichSpicyOrNot - custom-2':
            order_item = {
                'food_item': 'Chicken Sandwich',
                'quantity': 1
            }
            orders[session_id].append(order_item)
            print(f"Added to order: {order_item}")
            return jsonify({
                'fulfillmentText': f"Sure, I have added a Chicken Sandwich to your order."
            })

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
            return jsonify({
                'fulfillmentText': f"Here's your current order:\n{order_summary}\nTotal: ${total_price:.2f}"
            })

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
                order_summary += f"{quantity} x {food_item}\n"
            
            total_price = calculate_total(order_items)
            return jsonify({
                'fulfillmentText': f"Thank you for your order! Here's what you ordered:\n{order_summary}\nTotal: ${total_price:.2f}\nWould you like to confirm your order?"
            })

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
            return jsonify({
                'fulfillmentText': f"Your order has been confirmed! Here's what you ordered:\n{order_summary}\nTotal: ${total_price:.2f}\nThank you for choosing Chick-fil-A!"
            })

        elif intent_name == 'Default Welcome Intent':
            return jsonify({
                'fulfillmentText': "Welcome to Chick-fil-A! How can I help you today?"
            })
        
        else:
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

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')

    # Send the message to Dialogflow
    response = detect_intent_texts(
        'your-project-id', 'unique-session-id', [user_message], 'en-US')

    # Extract the reply
    bot_reply = response.query_result.fulfillment_text
    return jsonify({'reply': bot_reply})

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


def calculate_total(order_items):
    total_price = 0.0
    for item in order_items:
        item_name = item['food_item']
        quantity = item.get('quantity', 1)
        item_price = price_list.get(item_name, 0.0)
        total_price += item_price * quantity
    return round(total_price, 2)


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        print("\n=== WEBHOOK REQUEST ===")
        req = request.get_json(silent=True, force=True)
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

        if intent_name == 'OrderFood':
            food_items = parameters.get('FoodItem', [])
            quantity = parameters.get('number', 1)

            if not quantity:
                quantity = 1

            if isinstance(food_items, list) and food_items:
                food_item = food_items[0]
            else:
                food_item = str(food_items)

            if 'chicken sandwich' in food_item.lower():
                return jsonify({
                    'fulfillmentText': "Would you like your chicken sandwich original or spicy?"
                })

            order_item = {
                'food_item': food_item,
                'quantity': quantity
            }
            orders[session_id].append(order_item)
            print(f"Added to order: {order_item}")

            return jsonify({
                'fulfillmentText': f"Great! I've added {quantity} {food_item} to your order. Would you like anything else?"
            })

        elif intent_name == 'SandwichSpicyOrNot':
            return jsonify({
                'fulfillmentText': "Would you like your chicken sandwich original or spicy?"
            })

        elif intent_name == 'SandwichSpicyOrNot - custom':
            order_item = {
                'food_item': 'Spicy Chicken Sandwich',
                'quantity': 1
            }
            orders[session_id].append(order_item)
            print(f"Added to order: {order_item}")
            return jsonify({
                'fulfillmentText': "Great! I've added a Spicy Chicken Sandwich to your order. Would you like anything else?"
            })

        elif intent_name == 'SandwichSpicyOrNot - custom 2':
            order_item = {
                'food_item': 'Chicken Sandwich',
                'quantity': 1
            }
            orders[session_id].append(order_item)
            print(f"Added to order: {order_item}")
            return jsonify({
                'fulfillmentText': "Great! I've added a Chicken Sandwich to your order. Would you like anything else?"
            })

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
            return jsonify({
                'fulfillmentText': f"Here's your current order:\n{order_summary}\nTotal: ${total_price:.2f}"
            })

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
                order_summary += f"{quantity} x {food_item}\n"

            total_price = calculate_total(order_items)
            return jsonify({
                'fulfillmentText': f"Thank you for your order! Here's what you ordered:\n{order_summary}\nTotal: ${total_price:.2f}\nWould you like to confirm your order?"
            })

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
            return jsonify({
                'fulfillmentText': f"Your order has been confirmed! Here's what you ordered:\n{order_summary}\nTotal: ${total_price:.2f}\nThank you for choosing Chick-fil-A!"
            })

        elif intent_name == 'Default Welcome Intent':
            return jsonify({
                'fulfillmentText': "Welcome to Chick-fil-A! How can I help you today?"
            })

        else:
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
#     return jsonify({'reply': bot_reply})
