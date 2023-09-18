#GET REQUEST
from flask import Flask , request, jsonify
app = Flask(__name__)

@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    return "this is my first function for get {}".format(get_name)

#if __name__=='__main__':
   # app.run(port=5002)
#my default, when you do  not specify GET orr POST, it works with GET.
#run the above code and input http://127.0.0.1:5002/testfun?get_name=oluyege%20esther in your browser to get a result.
#GET is passing a data through a browser in an unsecured mode.

@app.route("/testingget")
def test1():
    get_name1 = request.args.get("get_name1")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get("mail_id")
    return "this is my first function for get {} {} {}".format(get_name1 ,mobile_number ,mail_id)

if __name__=='__main__':
    app.run(port=5003)
#the above code is for multiple characters
#http://127.0.0.1:5003/testingget?get_name1=oluyege%20esther%20&mobile=08134186524%20&mail_id=hiphester@gmail.com



