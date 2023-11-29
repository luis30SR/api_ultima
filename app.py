from flask import Flask
from config import config 
from flask_cors import CORS

#routes

from routes import movie


app = Flask(__name__)

CORS(app,resources={"*":{"origins": "http://localhost:9300"}})

def pagina_no_encontrada(error):
    return "<h1> pagina no encontrada</h1>",404
if __name__=='__main__':
    app.config.from_object(config['development'])

#blueprints
app.register_blueprint(movie.main, url_prefix='/api/movies')

#errores
app.register_error_handler(404, pagina_no_encontrada)
app.run()
