from flask import Flask, render_template
from models.user_01 import User, get_users


app = Flask(__name__)



@app.route('/')
def index():
    users_list = get_users
    return render_template('index.html',
                           users = users_list)

@app.route('/user/profile/<id>')
def user_profile(id):
    if id == '1':
        user_name = 'Pero Peric'
    elif id == '2':
        user_name = 'Ana Anic'
    else:
        user_name = 'Marko Markic'


    return render_template('user-profile.html',
                           user_id=user_name)


@app.route('/about-us')
def about_us():
    return render_template('about_us.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)

