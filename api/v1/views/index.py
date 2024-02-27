#!/usr/bin/python3
"""A module API test stats"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """The status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """The stats"""
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
        })
