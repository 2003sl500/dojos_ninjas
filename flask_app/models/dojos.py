from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas

DATABASE = 'dojos_ninjas'

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        # query = 'SELECT * from dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = 2;'
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos( name, updated_at ) VALUES( %(name)s, NOW() );"
        return connectToMySQL(DATABASE).query_db(query, data)