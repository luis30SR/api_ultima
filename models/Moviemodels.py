from database.db import get_conection
from .entities.Movie import Movie

class Moviemodel():

    @classmethod
    def get_movies(self):

        try:
            connection=get_conection()
            movies =[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id,titulo,duracion, lanzamiento FROM movie ORDER BY titulo ASC")
                resultset=cursor.fetchall()

                for row in resultset:
                    movie= Movie (row[0],row[1],row[2],row[3])
                    movies.append(movie.to_JSON())

            connection.close() 
            return movies

        except Exception as ex:
            raise Exception (ex)
        
    @classmethod
    def get_movie(self, id):

        try:
            connection=get_conection()
            

            with connection.cursor() as cursor:
                cursor.execute("SELECT id,titulo,duracion, lanzamiento FROM movie WHERE id= %s",(id,))
                row=cursor.fetchone()

                movie=None
                if row != None:
                   movie= Movie (row[0],row[1],row[2],row[3])
                   movie = movie.to_JSON() 

            connection.close() 
            return movie

        except Exception as ex:
            raise Exception (ex)  
        
    @classmethod
    def add_movie(self, movie):

        try:
            connection=get_conection()
            

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO movie (id,titulo,duracion,lanzamiento)
                               VALUES (%s,%s,%s,%s)""", (movie.id,movie.titulo,movie.duracion,movie.lanzamiento))
                affected_rows=cursor.rowcount
                connection.commit()

                
            connection.close() 
            return affected_rows

        except Exception as ex:
            raise Exception (ex)  


    @classmethod
    def update_movie(self, movie):

        try:
            connection=get_conection()
            

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE movie SET titulo = %s, duracion = %s, lanzamiento = %s
                               WHERE id = %s""", (movie.titulo, movie.duracion, movie.lanzamiento, movie.id))
                affected_rows=cursor.rowcount
                connection.commit()

                
            connection.close() 
            return affected_rows

        except Exception as ex:
            raise Exception (ex)             

    @classmethod
    def delete_movie(self, movie):

        try:
            connection=get_conection()
            

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM movie WHERE id = %s",(movie.id,))
                affected_rows=cursor.rowcount
                connection.commit()

                
            connection.close() 
            return affected_rows

        except Exception as ex:
            raise Exception (ex)  
