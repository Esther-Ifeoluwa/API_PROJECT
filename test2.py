#TASK
#write a program to insert a record in sql table via api database
#write a program to update a record via api
#write a program to delete a record via api
#write a program to fetch a record via api
#Answer the above questions for mongodb as well

#solution1
from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)


mydb = conn.connect(host = "localhost" , user = "root" , password = "IfeoluwA_04")
cursor = mydb.cursor()
cursor.execute("create database if not exists oyedeji")
cursor.execute("create table if not exists oyedeji.myowntable(name varchar(30), number int)")

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
       name = request.json['name']
       number= request.json['number']
       cursor.execute("insert into oyedeji.myowntable values(%s, %s)" , (name, number))
       mydb.commit()
       return jsonify(str('successfully inserted'))

#if __name__=='__main__':
   # app.run()

#Solution2
@app.route('/update',methods =['POST'])
def update():
    if request.method=='POST':
        get_name = request.json['get_name']
        cursor.execute("update oyedeji.myowntable set number = number - 5 where name = %s ",(get_name,))
        mydb.commit()
        return jsonify(str("succesfully updated"))

#if __name__=='__main__':
#  app.run()
#Go on postman and type what is below
#{
#    "get_name":"Toluwanimi"
#}


#Solution3

@app.route('/delete',methods =['POST'])
def delete():
    if request.method=='POST':
        name_del = request.json['name_del']
        cursor.execute("delete from oyedeji.myowntable where name = %s", (name_del,))
        mydb.commit()
        return jsonify(str("succesfully deleted"))

#if __name__=='__main__':
 #   app.run()

#solution4
#To fetch one record
@app.route('/fetch',methods =['POST'])
def fetch():
     cursor.execute("select * from oyedeji.myowntable")
     for i in cursor.fetchall():
        return jsonify(str(i))

#if __name__=='__main__':
 #   app.run()

#to fetch all the records
@app.route('/fetch_all',methods =['POST'])
def fetch_all():
     cursor.execute("select * from oyedeji.myowntable")
     l = []
     for i in cursor.fetchall():
         l.append(i)
     return jsonify(str(l))

#if __name__=='__main__':
  #  app.run()






