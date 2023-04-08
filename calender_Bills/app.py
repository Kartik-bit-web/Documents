from flask import Flask, render_template, url_for, request, redirect
import sqlalchemy as db


app = Flask(__name__)

    

@app.route('/')
def hel():
    return render_template('myindex.html')

@app.route('/event')
def event():
    error = 'Fill the form'
    return render_template('createEvent.html', error = error)

@app.route('/showBooking')
def booking():
    #qury = db.select(engin)
    return render_template('showBooking.html')

@app.route('/eve', methods=["POST"])
def eve():
    dat = request.form.get('date')
    opts = request.form.get('opt')
    nm = request.form.get('on')
    nums = request.form.get('num')
    if dat=='' and nums== '' and nm=='':
        return redirect('/event')
    else: 
        #x = db.insert(profile).values(dated= dat, opt= opts, name=nm, num=nums)
        #result = conaction.execute(x)
        #print(result)
        return redirect('/')
    
    return redirect('/event')

#db.create_all(engin)