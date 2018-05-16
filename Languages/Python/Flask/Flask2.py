from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def index():
    return "Method Used: %s"%request.method

@app.route('/bacon',methods=[
    'GET',
    'POST',
])
def bacon():
    if request.method=='GET':
        return "Method Using: Get"
    else:
        return "Method using : post"

if __name__=='__main__':
    app.run(debug=True)