from flask import Flask, render_template
from data import Artilces
app=Flask(__name__)

@app.route('/')
Articles=Articles()

@app.route('/')
def index():
    return render_template('user.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',articles=articles)

@app.route('/articles/<string:id>')
def articles(id):
    return render_template('articles.html',id=id)

if __name__=='__main__':
    app.run(debug=True)