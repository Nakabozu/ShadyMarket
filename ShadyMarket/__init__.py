from flask import Flask
app = Flask(__name__)

print("Initializing views")

import ShadyMarket.views

print("Views initialized successfully")
