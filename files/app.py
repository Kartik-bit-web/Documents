from flask import *
from fileinput import filename
from distutils.log import debug

app = Flask(__name__)

@app.route('/')
def hel():
    return render_template('index.html')

@app.route('/sucess', methods = ['POST'])
def sucess():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template('know.html', name=f.filename)
