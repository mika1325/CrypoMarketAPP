from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    return '<h1>INDEX PAGE</h1><p>Lorem ipsum dokor sit... </p>'


@app.route('/about-us')
def about_us():
    return '<h1>O nama<h1><p>Ovo je stranica koja opisuje cemu sluzi ova Web aplikacija</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)

