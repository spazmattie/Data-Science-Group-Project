
from flask import Flask, request

app = Flask(__name__, static_url_path='', static_folder='')

@app.route('/')
def root():
    return app.send_static_file("index.html")

"""
@app.route('/penny')
def penny():
    return app.send_static_file("penny.html")

@app.route('/name')
def name():
    return app.send_static_file("name.html")

@app.route('/event')
def event():
    return app.send_static_file("event.html")

print ("My name is Matthew Smith")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    """