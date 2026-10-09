from pymongo import MongoClient
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(
    dotenv_path=BASE_DIR / "atlas-credentials.env"
)

MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_URI = os.getenv("MONGODB_URI")

if MONGODB_USERNAME is None or MONGODB_PASSWORD is None or MONGODB_URI is None:
    raise Exception("Missing environment variables")

# user = MONGODB_USERNAME
# password = MONGODB_PASSWORD # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXCERCISE - 2
host = MONGODB_URI
# host = "mongodb+srv://pablogarciajuanes_db_user:{MONGODB_PASSWORD}@clusterflask.0smgbun.mongodb.net/?appName=ClusterFlask"
#create the connection url
# connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)
connecturl = host

uri = os.getenv("MONGODB_CERT_URI")
cert_file = os.getenv("MONGODB_CERT_PATH")

if not uri or not cert_file:
    raise ValueError("Falta la URI o la ruta del certificado")

cert_path = BASE_DIR / cert_file

if not cert_path.is_file():
    raise FileNotFoundError(cert_path)

try:
    with MongoClient(
        uri,
        authMechanism="MONGODB-X509",
        authSource="$external",
        tls=True,
        tlsCertificateKeyFile=str(cert_path),
        serverSelectionTimeoutMS=10000
    ) as connection:

        # Verificar conexión y autenticación
        connection.admin.command("ping")

        print("Conectado correctamente a MongoDB Atlas")

        # Consultar bases de datos
        dbs = connection.list_database_names()

        for db in dbs:
            print(f" - {db}")

except Exception as error:
    print(f"Error de conexión: {error}")

# connect to mongodb server
# def connection_mongodb():
#     print("Connecting to mongodb server")
#     connection = MongoClient(connecturl)
#     if connection is not None:
#         # print(connection)
#         print("Connected to the mongodb server")
#     return connection

# connection = connection_mongodb()


# get database list
# print("Getting list of databases")
# dbs = connection.list_database_names()

# print the database names

# for db in dbs:
#     print(db)
print("Closing the connection to the mongodb server")

# close the server connecton
connection.close()