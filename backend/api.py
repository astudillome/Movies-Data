import os
import json
from flask import Flask, render_template, jsonify, abort
from models import *
from auth.auth import AuthError, requires_auth
from app import app

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/movies', methods=['GET'])
def movies():
    # try:
    #     movies = Movie.query.order_by(Movie.id)
    #     if len(movies) == 0:
    #         abort(404)
    #     else:
    #         movies_summary = [movie.short() for movie in movies]
    #         return render_template('movies.html', movies=movies_summary)
    # except Exception as error:
    #     abort(404)
    return render_template('movies.html')


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": AuthError,
        "message": "Auth Error"
    }), AuthError
    
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource Not Found"
    }), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": 'Internal Server Error'
    }), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": 'Bad Request'
    }), 400

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": 'Method Not Allowed'
    }), 405