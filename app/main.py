from flask import Flask
import os

def pebble_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return f"hello world from app commit number: {os.getenv('COMMIT_SHA')} "

    return app
