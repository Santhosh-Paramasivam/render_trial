import os
from flask import Flask, jsonify, request
from ably import AblyRealtime

app = Flask(__name__)

# Initialize Ably Realtime client
ably_client = AblyRealtime(os.getenv('ABLY_KEY'))

# Set up Ably channel for real-time messaging
channel = ably_client.channels.get('trial')

@app.route('/')
def home():
    return "Flask App with Ably Realtime!"

@app.route('/publish', methods=['POST'])
def publish_message():
    message_data = request.json.get('message', 'Hello from Flask!')
    channel.publish("test", message_data)
    return jsonify({"status": "Message published!"})

# Subscribe to messages on the Ably channel
def subscribe_to_channel():
    channel.subscribe(lambda message: print(f"Received message: {message.data}"))

@app.before_first_request
def start_subscription():
    subscribe_to_channel()

if __name__ == '__main__':
    app.run(debug=True)
