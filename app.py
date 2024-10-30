from flask import Flask, request, jsonify
import ably
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "1 + 2 = 3"

if __name__ == '__main__':
    app.run(debug=True)
