import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eieblkmflrccfl:ca5db42257639a4f65b35f3bd3487712d10c16de29e54e17028deec3ee217ae3@ec2-54-236-169-55.compute-1.amazonaws.com:5432/d3pp7covc0vu0v'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', name='Cam & Lauren')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # admin = User(name='admin', email='admin@example.com')
    # db.session.add(admin)
    # db.session.commit()
    app.run(debug=True)