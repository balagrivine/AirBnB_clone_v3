#!/usr/bin/python3

from flask import Flask, Blueprint
from models import view
from app_views import api.v1.views

app = Flask(__name__)

app_views = Blueprint('app_views', __name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def tear_down():
    """method to handle @app.teardown_appcontext"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', host=5000, threaded=True)

