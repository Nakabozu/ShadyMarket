import os
from ShadyMarket import app

exec("./ShadyMarket/app.py")

port = int(os.environ.get('PORT', 33507))
app.run(host='0.0.0.0', port=port)
