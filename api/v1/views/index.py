#!/usr/bin/python3

from api.v1.views import app_views
import jsonify

@app_views.route('/status')
def status_code():
    """returns a JSON"""
    return jsonify({"status":"OK"})
