import pymongo
import certifi

con_str = "mongodb+srv://letherius:demarco17@cluster0.afdqha3.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("OrganikaLetherius")

me = {
    "first": "Letherius",
    "last": "Miller",
    "age": 31,
    "hobbies": [],
    "address": {
        "street": "Evergreen",
        "number": 742,
        "city": "Springfield"
    }
}