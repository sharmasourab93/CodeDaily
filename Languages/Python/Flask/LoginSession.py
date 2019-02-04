from flask import Flask,flash,redirect,render_template,request,session,abort,escape,url_for
from os import urandom

app=Flask(__name__)

app.debug=True
app.secret_key=urandom(24)

@app.route('/')
def index():
    if 'username' in session:
        return 'Hey,{}!'.format(escape(session['username']))
    return "You are not signed in!"
    
@app.route('/sign_in',methods=['GET','POST'])
def sign_in():
    if request.method=='POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
        <p> Username <input name="username">
        <p><button> Sign in</button></p>
        </form>
    '''

@app.route('/sign_out')
def sign_out():
    session.pop('username')
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)