import pymongo

class Database(object):

    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    # Tell Python we're not gonna use `self`
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        # Database.DATABASE contains the db for the project
        # and we can access it from other parts of the program
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)




    # Normally we do the init thing
    # def __init__(self):
    #     self.uri = ""
    #     self.database = None