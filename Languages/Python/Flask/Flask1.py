from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "This is the homepage"
@app.route('/tuna')
def tuna():
    return '<h1>Tuna is good</h1>'

@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s"%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post id is %d" % post_id

if __name__=='__main__':
    app.run(debug=True)
