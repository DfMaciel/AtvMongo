from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def conexao ():
    uri = "mongodb+srv://DaviMaciel:davimaciel2@cluster0.aggpb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    client = MongoClient(uri, server_api=ServerApi('1'))
    global db 
    global mycol
    db = client["Cluster0"]

    try:
        client.admin.command('ping')
        print("Conexão realizada!")
    except Exception as e:
        print(e)