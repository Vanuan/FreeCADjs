import re
import sys
import os

from flask.cli import main

sys.argv = ['', 'run', '--host=0.0.0.0']
os.environ['FLASK_APP'] = 'server'
#os.environ['FLASK_ENV'] = 'development'

sys.path.append(os.path.dirname(__file__))

sys.exit(main())