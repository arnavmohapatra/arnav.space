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

if __name__ == "__main__":
    #app.config['SERVER_NAME'] = 'arnav.space:5000'
    app.run(host='localhost', port=int(os.getenv("PORT", "8080")), debug=True)
    
    
#TODO:
# - Resize BG images to reduce load times
# - Fix BG Scaling
# - fix Button on index
# - Add resume
# - learn HTML    