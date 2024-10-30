import ably
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Initialize Ably Realtime client for WebSocket connection
ably_client = ably.AblyRealtime(os.getenv('ABLY_KEY'))

# Set up Ably channel for real-time messaging
# channel = ably_client.channels.get('trial')

@app.route('/')
def home():
    return "Flask App with Ably WebSockets for low latency!"

# Subscribe to messages on the Ably channel
#def subscribe_to_channel():
#    channel.subscribe(lambda message: print(f"Received message: {message.data}"))

# Run the subscription function when the app starts
#with app.app_context():
#    subscribe_to_channel()

if __name__ == '__main__':
    app.run(debug=True)
