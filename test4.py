#API mongotask from test3 file
from flask import Flask , request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://Ifeoluwa:<password>@ifeoluwa.hrs9tdw.mongodb.net/?retryWrites=true&w=majority")
database = client['oyedeji_family']
collection=database['oyedeji_family_names']


@app.route('/insertmongodb', methods=['POST'])
def insertmongodb():
    if request.method == 'POST':
       name = request.json['name']
       number = request.json['number']
       collection.insert_one({name:number})
       return jsonify(str("successfully inserted"))

if __name__ == "__main__":
    app.run(port=5001)     #a lot of API may be up and running so you may have to change the port name to 5001 if you do not want to restart pycharm



