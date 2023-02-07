import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi #it provides Mozilla’s thoroughly curated collection of Root Certificates for validating the trustworthiness
 #of SSL certificates while verifying the identity of TLS hosts

ca=certifi.where()

class MongoDBClient:
    client = None
    def __init__(self,database_name= DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url="mongodb+srv://GauravM:Manori97@cluster0.qgrl2rk.mongodb.net/?retryWrites=true&w=majority"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
                self.client = MongoDBClient.client
                self.database = self.client[database_name]
                self.database_name = database_name
        except Exception as e:
            raise e
    


        
