from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__) # load config from this file , flaskr.py

import flaskr.flaskr.views
