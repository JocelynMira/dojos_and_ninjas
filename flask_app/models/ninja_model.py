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
    def one_ninja(cls,id):
        query = """SELECT * from ninjas
                WHERE id = %(id)s """
        results= connectToMySQL(cls.DB).query_db(query,{'id':id})
        return cls(results[0])

    # UPDATE
    @classmethod
    def update(cls, data):
        query = """UPDATE ninjas
                SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s
                WHERE id = %(id)s; """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    # DELETE
    @classmethod
    def delete(cls, id):
        query = """DELETE FROM ninjas
                WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, {'id': id})
        return results