import os
from threading import Thread

from ShadyMarket import app
from ShadyMarket import blanca

port = int(os.environ.get('PORT', 33507))
print("Creating Flask Process")
flaskProcess = Thread(target=lambda: app.run(host="0.0.0.0", port=23336, debug=False, use_reloader=False))
print("Creating Blanca Process")
blancaProcess = Thread(target=blanca.open_shop, name="blancaThread")

if __name__ == "__main__":
    print("Starting Flask Process")
    flaskProcess.start()
    print("Starting Blanca Process")
    blancaProcess.start()

    flaskProcess.join()
    blancaProcess.join()
