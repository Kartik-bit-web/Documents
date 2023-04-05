from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def hel():
    return render_template('myindex.html')

@app.route('/event')
def event():
    return render_template('createEvent.html')

@app.route('/eve', methods = ['POST', 'GET'])
def eve():
    if request.method == 'POST':
        dat = request.form['date']
        opt = request.form['opt']
        nm = request.form['on']
        num = request.form['num']
        amut = request.form['amount']
        print(dat, opt, nm, num, amut)

    return 'works'