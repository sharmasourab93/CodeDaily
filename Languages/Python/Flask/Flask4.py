from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html",user=user)
if __name__=='__main__':
    app.run()