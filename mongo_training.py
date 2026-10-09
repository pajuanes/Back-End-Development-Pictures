from pymongo import MongoClient
from mongo_connect import connecturl
from pymongo.errors import CollectionInvalid


# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

db_name="training"
collection = "mongodb_glossary"

db = connection[db_name]

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