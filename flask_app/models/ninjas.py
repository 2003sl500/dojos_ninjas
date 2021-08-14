from flask.globals import session
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_ninjas'

class Ninjas:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas( first_name, last_name, age, updated_at, dojo_id ) VALUES( %(first_name)s, %(last_name)s, %(age)s, NOW(), %(dojo_id)s );"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def show_dojo_ninjas(cls, id):
        query = 'SELECT * from dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        # query = "SELECT * FROM ninjas"
        data = {
            "id": id
        }
        results = connectToMySQL(DATABASE).query_db(query, data)
        print("************ results: ", results)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos