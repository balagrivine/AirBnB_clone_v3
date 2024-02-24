#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status')
def status():
    """returns a JSON"""
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/stats')
def number_objects():
    """Retrieves the number of each objects by type"""
    data = models.storage.all(cls)
    for k, v in data.items():
        return jsonify(v: storage.count(v))
