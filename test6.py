from flask import Flask , request, jsonify
import mysql.connector as conn
app = Flask(__name__)

mydb = conn.connect(host = "localhost" , user = "root" , password = "IfeoluwA_04")
cursor = mydb.cursor()
cursor.execute("create database if not exists oyedeji")
cursor.execute("create table if not exists oyedeji.myowntable(name varchar(30), number int)")



@app.route('/get_data')
def get_data_from():
    db = request.args.get('db')
    tbl = request.args.get('tbl')
    try:
        mydb = conn.connect(host="localhost", user="root", password="IfeoluwA_04", database=db)
        cursor = mydb.cursor(dictionary=True)
        cursor.execute(f'select * from {tbl}')
        data = cursor.fetchall()
        mydb.commit()
        mydb.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__=='__main__':
   app.run(port=5004)
#Running the above code and inputing the url with the database name and table name below gives a list of the info in the databse and table.
#http://127.0.0.1:5004/get_data?db=oyedeji%20&tbl=myowntable