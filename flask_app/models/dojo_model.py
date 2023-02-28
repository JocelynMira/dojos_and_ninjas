from flask_app.config.mysqlconnection import connectToMySQL
from .ninja_model import Ninja



class Dojo:
    
    DB= "dojos_and_ninjas"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    # CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos (name)
                VALUES ( %(name)s )"""
        return connectToMySQL(cls.DB).query_db(query,data)

    # READ 
    @classmethod
    def get_dojos(cls):
        query = """SELECT * FROM dojos"""
        dojos_from_db = connectToMySQL(cls.DB).query_db(query) #results comes in a list of dictionaries
        dojos = []

        for dojo in dojos_from_db:
            dojos.append (cls (dojo) )
        return dojos


    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """SELECT * FROM dojos
        LEFT JOIN ninjas on dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojo = cls (results [0])
        
        for row_from_db in results:

            ninja_info = {
                "id" : row_from_db['ninjas.id'],
                "first_name": row_from_db['first_name'],
                "last_name": row_from_db['last_name'],
                "age": row_from_db['age'],
                "created_at": row_from_db['ninjas.created_at'],
                "updated_at": row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(ninja_info))
        return dojo



