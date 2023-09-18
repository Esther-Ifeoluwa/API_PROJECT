from flask import  Flask , request, jsonify

app = Flask(__name__)

@app.route('/abcd',methods=['GET' , 'POST'])
def test1():
    if(request.method=='POST'): #This means if someone is trying to send a data in a body, perform the next operation
        a = request.json['num1']  #ask someone to send a data in json format to my system
        b = request.json['num2']
        result = a + b
        return jsonify((str(result)))

if __name__=='__main__':
    app.run()

