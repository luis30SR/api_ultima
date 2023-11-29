from utils.DateFormat import DateFormat
class Movie():

    def __init__(self,id,titulo= None,duracion=None,lanzamiento=None,) -> None:
       self.id = id
       self.titulo = titulo
       self.duracion = duracion
       self.lanzamiento = lanzamiento
    
    def to_JSON(self):
        return{
            'id':self.id,
            'titulo': self.titulo,
            'duracion':self.duracion,
            'lanzamiento': DateFormat.convert_data(self.lanzamiento)
        }   
       

 