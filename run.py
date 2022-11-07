import os
import subprocess

from ShadyMarket import app
from ShadyMarket import blanca


port = int(os.environ.get('PORT', 33507))
app.run(host='0.0.0.0', port=port)
subprocess.call(blanca)