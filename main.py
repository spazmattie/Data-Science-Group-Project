
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/index', static_folder='')

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    
@app.route('/penny')
def penny():
    return app.send_static_file("penny.html")

@app.route('/name')
def name():
    return app.send_static_file("name.html")

@app.route('/event')
def event():
    return app.send_static_file("event.html")

@app.route('/hello')
def hello():
    name = "Matthew"
    html = "<html><title>Welcome Page</title><body>Hello "
    html += name
    html += "</body></html>"
    return make_response(html)

print ("My name is Matthew Smith")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)