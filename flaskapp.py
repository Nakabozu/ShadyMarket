from flask import Flask

app = Flask(__name__)


async def async_blanca():
    exec("./app.py")


@app.route("/")
def index():
    return "What are you doing here?!?  Get out of my house!"
