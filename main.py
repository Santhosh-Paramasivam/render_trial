from flask import Flask, request, jsonify
import ably
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Ably app!"

if __name__ == '__main__':
    app.run(debug=True)
