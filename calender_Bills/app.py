from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dated = db.Column(db.String(50), nullable=False)
    opt = db.Column(db.String(50), nullable=False)
    name = db.Column(db.Integer, nullable=False)
    num = db.Column(db.Integer, nullable=False)
    
    def __repr__(self, id, dated, opt, name, num):
        self.id = id
        self.dated = dated
        self.opt = opt
        self.name = name
        self.num = num
    
 

@app.route('/')
def hel():
    return render_template('myindex.html')

@app.route('/event')
def event():
    return render_template('createEvent.html')

@app.route('/eve', methods=["POST"])
def eve():
    dat = request.form.get('date')
    opts = request.form.get('opt')
    nm = request.form.get('on')
    nums = request.form.get('num')
    x = Profile(dated= dat, opt= opts, name=nm, num=nums)
    db.session.add(x)
    db.session.commit()

    return 'works'

db.create_all()