
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

@app.route('/')
@app.route('/name', methods=['GET', 'POST'])
def name():
    print('get req: ', request.args.get)
    author_list = list(['Matt', 'Sam', 'Steven'])
    author = request.args.get('author')
    if author is None:
        errorMsg = 'Please enter an author name.'
        author = ''
    elif author in author_list:
        errorMsg = ''
        print('author: ', author)
    else:
        errorMsg = 'Please enter a VALID author name.'
    html = render_template('name.html',
        errorMsg=errorMsg,
        author=author)
    response = make_response(html)
    return response

@app.route('/roi', methods=['GET'])
def roi():
    net_roi = request.args.get('net-roi')
    coi = request.args.get('coi')
    ROI = (int(net_roi)/int(coi)) * 100
    print ('ROI: ', ROI)
    html = render_template('name.html', ROI=str(ROI))
    response = make_response(html)
    return response


"""
@app.route('/name')
def name():
    return app.send_static_file("name.html")
"""

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