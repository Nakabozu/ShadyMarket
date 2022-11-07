from ShadyMarket import app

print("Opening views")

@app.route('/')
def index():
    return 'What are you doing here?!?  Get out of my house!'