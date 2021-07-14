import os
import json
from flask import Flask, render_template, request, jsonify, abort
from models import *
# from .auth.auth import AuthError, requires_auth
from app import app


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        movies = Movie.query.order_by(Movie.id)
        if len(movies) == 0:
            abort(404)
        else:
            movies_summary = [movie.short() for movie in movies]
            return jsonify({
                'success': True,
                'movies': movies_summary
                }), 200
    except Exception as error:
        abort(404)