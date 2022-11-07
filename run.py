import os
import sys
from ShadyMarket import app

exec(os.path.join(os.path.dirname(sys.argv[0]), 'ShadyMarket', 'app.py'))
port = int(os.environ.get('PORT', 33507))
app.run(host='0.0.0.0', port=port)
