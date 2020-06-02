from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template
from flask import url_for
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    #app.config['SERVER_NAME'] = 'arnav.space:5000'
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", "8080")), debug=True)