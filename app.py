#venv/bin/python app.py to run app
# ngrok http 5001    

from flask import Flask, request, jsonify, render_template
from static_data import price_list, item_name_mapping, size_required_items, menu_items
from flask_cors import CORS
import os
import json
import dialogflow_v2 as dialogflow
from google.oauth2 import service_account
from google.auth.credentials import Credentials
import json



app = Flask(__name__)
CORS(app)

# Global storage for orders
orders = {}
last_ordered_item = {}


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


# Dialogflow service account key (replace with your key as a string)
service_account_key = """{
  "type": "service_account",
  "project_id": "fast-food-chatbot",
  "private_key_id": "477fd4de4ea96de8d4d706310d962aa514c0dbdd",
  "private_key": "-----BEGIN PRIVATE KEY-----\\n477fd4de4ea96de8d4d706310d962aa514c0dbdd\\n-----END PRIVATE KEY-----\\n",
  "client_email": "sharunnaicker@gmail.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "your-client-x509-cert-url"
}"""

# Parse the JSON key
service_account_info = json.loads(service_account_key)
credentials = Credentials.from_service_account_info(service_account_info)

# Dialogflow project ID
project_id = service_account_info["fast-food-chatbot"]


def detect_intent_texts(project_id, session_id, text, language_code):
    """Send a text query to Dialogflow and return the result."""
    session_client = dialogflow.SessionsClient(credentials=credentials)
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    return response.query_result.fulfillment_text


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        req = request.get_json(silent=True, force=True)
        user_message = req.get('message')

        if user_message:
            # Process the user's message
            bot_response = f"You said: {user_message}"  # Example response
            return jsonify({'fulfillmentText': bot_response})
        
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
#     return jsonify({'reply': bot_reply})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
