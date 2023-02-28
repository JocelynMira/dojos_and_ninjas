from flask_app.config.mysqlconnection import connectToMySQL



class Ninja:
    DB = "dojos_and_ninjas"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id)
                VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s )"""
        # this query will retrun an id
        return connectToMySQL(cls.DB).query_db(query,data)


    # READ 
    @classmethod
    def get_ninjas(cls):
        query = """SELECT * FROM ninjas"""
        ninjas_from_db = connectToMySQL(cls.DB).query_db(query)
        print('ninjas', ninjas_from_db)
        ninjas = []

        for ninja in ninjas_from_db:
            ninjas.append (cls (ninja) )
        return ninjas

    @classmethod
    def get_one_ninja(cls, id):
        query = """SELECT * FROM dojos LEFT JOIN
                ninjas ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s """
        results = connectToMySQL(cls.DB).query_db(query, {"id": id})
        dojo = cls (results[0])

        for ninja in results:
            ninja_info = {
                'id' : ninja['id'],
                'first_name' : ninja['first_name'],
                'last_name' : ninja['last_name'],
                'age' : ninja['age'],
                'created_At' : ninja['created_at'],
                'updated_at' : ninja['updated_at'],
                'dojo_id' : ninja['dojo_id']
            }
            dojo.ninjas.append(Ninja(ninja_info))
        print (ninja_info)
        return ninja



