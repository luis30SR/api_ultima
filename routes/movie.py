from flask import Blueprint, jsonify, request
import uuid
#entities
from models.entities.Movie import Movie

#modelos
from models.Moviemodels import Moviemodel

main= Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        movies=Moviemodel.get_movies()
        return jsonify(movies)

    except Exception as ex: 

        return jsonify ({'mensaje': str(ex)}),500

@main.route('/<id>')
def get_movie(id):
    try:
      movie=Moviemodel.get_movie(id)
      if movie != None:
          return jsonify(movie)
      else:
          return jsonify({}), 404
    except Exception as ex: 
        return jsonify ({'mensaje': str(ex)}),500
    
@main.route('/add', methods=['POST'])
def add_movie():
    try:
        titulo=request.json['titulo']
        duracion= int (request.json['duracion'])
        lanzamiento=request.json['lanzamiento']
        id= uuid.uuid4()
       
        movie=Movie(str(id),titulo,duracion,lanzamiento)
        affected_rows = Moviemodel.add_movie(movie)
        if affected_rows==1:
          return jsonify(movie.id)
        else:
            return jsonify ({'mensaje': "Error insert"}),500  
     
    except Exception as ex: 
        return jsonify ({'mensaje': str(ex)}),500   
    
@main.route('/update/<id>', methods=['PUT'])

def update_movie(id):
    try:
        titulo=request.json['titulo']
        duracion= int (request.json['duracion'])
        lanzamiento=request.json['lanzamiento']
        movie=Movie(id,titulo,duracion,lanzamiento)
        affected_rows = Moviemodel.update_movie(movie)
        if affected_rows==1:
          return jsonify(movie.id)
        else:
            return jsonify ({'mensaje': "No movie update"}),404
     
    except Exception as ex: 
        return jsonify ({'mensaje': str(ex)}),500   



@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie= Movie(id)
        affected_rows = Moviemodel.delete_movie(movie)

    
        if affected_rows==1:
          return jsonify(movie.id)
        else:
            return jsonify ({'mensaje': "No movie deleted"}),404
     
    except Exception as ex: 
        return jsonify ({'mensaje': str(ex)}),500      
    

