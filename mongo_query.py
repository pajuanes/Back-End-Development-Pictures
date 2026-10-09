from pymongo import MongoClient
# from mongo_connect import connection_mongodb
from mongo_connect import connecturl
from pymongo.errors import CollectionInvalid

# user = 'root'
# password = 'MjQwOTgtcnNhbm5h' # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXCERCISE - 2
# host='mongo'
#create the connection url
# connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# connecturl = connection_mongodb()

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)


connection.admin.command("ping")

collection = "training"

db = connection[collection]

if collection in connection.list_database_names():
    print(f"La base de datos '{db.name}' ya existe.")
else:
    # Seleccionar una base no la crea: crear una colección sí.
    try:
        db.create_collection(collection)
        print(f"Base de datos '{db.name}' creada con la colección '{collection}'.")
    except CollectionInvalid:
        # Otro proceso podría haber creado la colección entretanto.
        print(f"La colección '{collection}' ya existe.")

# collection = db[collection]

# select the 'training' database 

# db = connection.training

# select the 'python' collection 

# collection = db.python

# create a sample document

doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases"}

# insert a sample document

print("Inserting a document into collection.")
db[collection].insert_one(doc)

# query for all documents in 'training' database and 'python' collection

docs = db[collection].find()

print("Printing the documents in the collection.")

for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
connection.close()