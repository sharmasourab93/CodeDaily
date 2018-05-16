from flask import Flask,render_template

app=Flask(__name__)

@app.route("/shopping")
def shoping():
    food=["Cheese","Tuna","Fish"]
    return render_template("shopping.html", food=food)
if __name__=='__main__':
    app.run()