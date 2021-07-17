import os
import json
from flask import Flask, jsonify, abort, request
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

@app.route('/actors', methods=['GET'])
def get_actors():
    try:
        actors = Actor.query.order_by(Actor.id).all()
        if len(actors) == 0:
            abort(404)
        else:
            actors_summary = [actor.short() for actor in actors]
            return jsonify({
                'success': True,
                'actors': actors_summary
                })
    except Exception as error:
        abort(422)
        
@app.route('/actors', methods=["POST"])
@requires_auth('post:actors')
def add_actors(payload):
    data = request.get_json()
    new_name = data.get('name', None)
    new_age = data.get('age', None)
    new_gender = data.get('gender', None)
    new_actor = []
    
    try:
        new_actor = Actor(name=new_name, age=new_age, gender=new_gender)
        new_actor.insert()
        
        return jsonify({
            'success': True,
            'actor': Actor.long(new_actor)
        }), 200
        
    except Exception as error:
        abort(422)

@app.route('/actors/<int:id>', methods=['PATCH'])
@requires_auth('patch:actors')
def edit_actor(token, id):
    data = request.get_json()
    edited_name = data.get('name', None)
    edited_age = data.get('age', None)
    edited_gender = data.get('gender', None)
    
    try:
        edited_actor = Actor.query.filter(Actor.id == id).one_or_none()
        if len(edited_actor) == 0:
            abort(404)
        edited_actor.name = edited_name
        edited_actor.age = edited_age
        edited_actor.gender = edited_gender
        edited_actor.update()
        
        return jsonify({
            'success': True,
            'actor': edited_actor.long()
        }), 200
        
    except Exception as error:
        abort(422)
        
@app.route('/actors/<int:id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(token, id):
    try:
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if len(actor) == 0:
            abort(404)
        else:
            actor.delete()
            return jsonify({
                'success': True,
                'delete': id
            }), 200
            
    except Exception as error:
        abort(422)
@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        movies = Movie.query.order_by(Movie.id).all()
        if len(movies) == 0:
            abort(404)
        else:
            movies_summary = [movie.short() for movie in movies]
            return jsonify({
                'success': True,
                'movies': movies_summary
                })
    except Exception as error:
        abort(422)
@app.route('/movies', methods=["POST"])
@requires_auth('post:movies')
def add_movies(payload):
    data = request.get_json()
    new_title = data.get('title', None)
    new_release_date = data.get('release_date', None)
    new_movie = []
    
    try:
        new_movie = Movie(title=new_title, release_date=new_release_date)
        new_movie.insert()
        
        return jsonify({
            'success': True,
            'movie': Movie.long(new_movie)
        }), 200
        
    except Exception as error:
        abort(422)
@app.route('/movies/<int:id>', methods=['PATCH'])
@requires_auth('patch:movies')
def edit_movie(token, id):
    data = request.get_json()
    edited_title = data.get('title', None)
    edited_release_date = data.get('release_date', None)
    
    try:
        edited_movie = Movie.query.filter(Movie.id == id).one_or_none()
        if len(edited_movie) == 0:
            abort(404)
        edited_movie.title = edited_title
        edited_movie.release_date = edited_release_date
        edited_movie.update()
        
        return jsonify({
            'success': True,
            'movie': edited_movie.long()
        }), 200
        
    except Exception as error:
        abort(422)
        
@app.route('/movies/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(token, id):
    try:
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if len(movie) == 0:
            abort(404)
        else:
            movie.delete()
            return jsonify({
                'success': True,
                'delete': id
            }), 200
            
    except Exception as error:
        abort(422)

@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": AuthError,
        "message": "Auth Error"
    }), AuthError
    
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": 'Bad Request'
    }), 400
    
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource Not Found"
    }), 404
@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": 'Method Not Allowed'
    }), 405
@app.errorhandler(422)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable"
    }), 422

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": 'Internal Server Error'
    }), 500