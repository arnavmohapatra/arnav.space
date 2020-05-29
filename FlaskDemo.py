from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.config['SERVER_NAME'] = 'arnav.space:5000'
    app.run(debug=True)