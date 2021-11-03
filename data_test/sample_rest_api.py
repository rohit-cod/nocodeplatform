from pymongo import MongoClient
from flask import Flask
from flask import request
from flask_cors import CORS
import copy
import json

client = MongoClient('mongodb://cod:macmakmacmak00@cluster0-shard-00-00-haasx.azure.mongodb.net:27017,cluster0-shard-00-01-haasx.azure.mongodb.net:27017,cluster0-shard-00-02-haasx.azure.mongodb.net:27017/admin?ssl=true&ssl_cert_reqs=CERT_NONE&replicaSet=Cluster0-shard-0&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-1&3t.uriVersion=3&3t.connection.name=Chain+of+demand&3t.databases=admin,test')
#client = MongoClient('mongodb://23.98.41.87:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&3t.uriVersion=3&3t.connection.name=CodMongo2TB&3t.alwaysShowAuthDB=true&3t.alwaysShowDBFromUserRole=true')
#client = MongoClient('mongodb://demouser:Today123@23.97.66.7:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-256&3t.uriVersion=3&3t.connection.name=DemoPI&3t.alwaysShowAuthDB=true&3t.alwaysShowDBFromUserRole=true')

app = Flask(__name__)
CORS(app)
db = client.no_code_data

@app.route('/car_data')
def get_car_data():
    collection = db.car_data
    cursor = collection.find({})
    all_items=[]
    for document in cursor:
        tempdoc=copy.deepcopy(document)
        tempdoc.pop('_id')
        all_items.append(tempdoc)
    return json.dumps(all_items)

if __name__ == "__main__":
    app.run(host='0.0.0.0')