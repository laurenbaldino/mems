from flask import Flask, render_template


app = Flask(__name__)

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
    app.run(debug=True)