from flask import Flask, request
import requests

app = Flask(__name__)

# Replace these URLs with your and your friend's Ngrok URLs
YOUR_NGROK_URL = "https://93b4-153-33-34-165.ngrok-free.app/"
FRIEND_NGROK_URL = "https://5848-76-78-190-39.ngrok-free.app/webhook"

@app.route('/webhook', methods=['POST'])
def intermediate_webhook():
    # Get the request data from Dialogflow
    data = request.json

    # Forward the request to your webhook
    try:
        your_response = requests.post(YOUR_NGROK_URL, json=data)
        print(f"Forwarded to your webhook: {your_response.status_code}")
    except Exception as e:
        print(f"Error forwarding to your webhook: {e}")

    # Forward the request to your friend's webhook
    try:
        friend_response = requests.post(FRIEND_NGROK_URL, json=data)
        print(f"Forwarded to friend's webhook: {friend_response.status_code}")
    except Exception as e:
        print(f"Error forwarding to friend's webhook: {e}")

    # Respond back to Dialogflow
    return "Requests forwarded", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)  # Runs on port 5002
