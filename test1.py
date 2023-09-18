from flask import  Flask , request, jsonify
#Flask function helps you expose your functions to the outer world.

app = Flask(__name__)

@app.route('/abc',methods=['GET' , 'POST'])
def test1():
    if(request.method=='POST'): #This means if someone is trying to send a data in a body, perform the next operation
        a = request.json['num1']  #ask someone to send a data in json format to my system
        b = request.json['num2']
        result = a + b
        return jsonify((str(result))) #this means you should convert to a string format and return json


#if __name__=='__main__':  #Expose the def test1 function
   # app.run()

##Run the above code and Go to postman and paste the url appearing on the pycharm terminal on the Enter Request Url icon
#and add /abc. This helps you reach out to the server.
#On postman, click on post, body, raw, json and then pass your texts to your function and execute. Return back to pycharm and youll receive
#a command in your terminal which says 200 and this indicates that post is successful.
#E.g {
#        "num1":10 ,
#        "num2":20
#    }
#The result of the above in postman is 30.



#@app is the object called in line 3, route is a flask function and the command in the bracket is the set
#of rules to be passed inside the def test1. The abc is the url and the method mean we can send a data via
#GET or POST.
#GET is an inbuilt statement that means sending a data through url(data security is not important) and POST means sending a data
# via Body(maintains security)


@app.route('/abc1/oluyege',methods=['GET' , 'POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify((str(result)))

#Several functions can also be  called
@app.route('/abc1/oluyege/test3',methods=['GET' , 'POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a - b
        return jsonify((str(result)))

@app.route('/abc1/oluyege/test4',methods=['GET' , 'POST'])
def test4():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        return jsonify((str(result)))

if __name__=='__main__':
    app.run()

