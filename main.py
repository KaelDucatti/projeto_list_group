from flask import Flask, render_template, request


app = Flask(__name__)

def home():
    return "Hello"

if __name__ == "__main__":
    app.run(port=5152, debug=True, host="0.0.0.0")