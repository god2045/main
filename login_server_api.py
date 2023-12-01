from flask import Flask,jsonify,request
from flask_cors import CORS
login_server_api= Flask(__name__)
CORS(login_server_api)
login_server_api.config["JSON_AS_ASCII"]= False

@login_server_api.route("/hello",methods=['POST'])
def hello():
    user=request.json
    if (user["uname"]=="admin" and user["password"]=="123456"):
        return jsonify({"code":200,"msg":"用户名正确","url":"https://162.14.73.102:5000/index_1.html"})
    else:
        return jsonify({"code":201,"msg":"用户名错误"})

@login_server_api.route("/",methods=[ 'GET','POST'])
def index():
    return "Hello World!22222"

if __name__=='__main__':
    login_server_api.run(host='0.0.0.0',port=5000)

