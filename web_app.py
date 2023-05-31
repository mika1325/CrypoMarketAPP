from flask import Flask, render_template, jsonify
import requests

#from models.user_01 import User, get_users
from models.user import User
from services.db_repos.db_repo import db_init


app = Flask(__name__)


@app.route('/')
def index():
    #users_list = get_users()
    #return render_template('index.html', users = users_list)
    return render_template('index.html')


@app.route('/user/profile/<id>')
def user_profile(id):
    if id == '1':
        user_name = 'Pero Peric'
    elif id == '2':
        user_name = 'Ana Anic'
    else:
        user_name = 'Marko Maric'

    return render_template('user-profile.html',
                           user_id=user_name)


@app.route('/about-us/<id>')
def about_us(id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')

    if response.status_code == 200:
        user_from_dict = User.from_dict(response.json())

    return render_template('about_us.html', user_in_template = user_from_dict)


@app.route('/api/about-us/<id>')
def api_user(id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')

    if response.status_code == 200:
        user_from_dict = User.from_dict(response.json())
        user_from_dict.name = "Pero Peric"

    return jsonify(user_from_dict.company.__dict__)



if __name__ == '__main__':
    db_init()
    app.run(host='0.0.0.0', port=5000, debug=True)