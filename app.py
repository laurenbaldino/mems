import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/handle_login', methods=['POST'])
def handle_login():
    from models.User import User
    
    username = request.form['username_input']
    user = User.query.filter_by(email = username).first()
    if user:
        return "Logged in"
    return "username invalid"

@app.route('/profile')
def profile():
    return render_template('profile.html', name='Cam & Lauren')


if __name__ == '__main__':
    from models.User import User

    with app.app_context():
        db.create_all()

    app.run(debug=True)