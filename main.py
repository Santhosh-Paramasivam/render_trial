import os
import ably
from flask import Flask
from ably import AblyRealtime

app = Flask(__name__)

# Initialize Ably Realtime client for WebSocket connection
ably_client = AblyRealtime(os.getenv('ABLY_KEY'))

# Set up Ably channel for real-time messaging
channel = ably_client.channels.get('trial')

@app.route('/')
def home():
    return "Flask App with Ably WebSockets for low latency!"

# Subscribe to messages on the Ably channel
def subscribe_to_channel():
    channel.subscribe(lambda message: print(f"Received message: {message.data}"))

# Run the subscription function when the app starts
@app.before_first_request
def start_subscription():
    subscribe_to_channel()

if __name__ == '__main__':
    # Use Uvicorn to run the app instead of Flask's built-in server
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
