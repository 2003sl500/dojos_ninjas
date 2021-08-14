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

        # results pulls in dojo_id
        # print("***************", results)
        
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas( first_name, last_name, age, updated_at, dojo_id ) VALUES( %(first_name)s, %(last_name)s, %(age)s, NOW(), %(dojo_id)s );"
        print("***********", data)
        return connectToMySQL(DATABASE).query_db(query, data)