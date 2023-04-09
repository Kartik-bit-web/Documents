from flask import Flask, render_template, url_for, request, redirect
import sqlalchemy as db

app = Flask(__name__)
engin  = db.create_engine('sqlite:///my.db')
connection = engin.connect()
metadata = db.MetaData()

data = db.Table('info', metadata,
                db.Column('Id', db.Integer(), primary_key= True, autoincrement=True),
                db.Column('dated', db.String(50)),
                db.Column('option', db.String(50)),
                db.Column('name', db.String(50)),
                db.Column('number', db.Integer)
                )

@app.route('/')
def hel():
    return render_template('myindex.html')

@app.route('/event')
def event():
    error = 'Fill the form'
    return render_template('createEvent.html', error = error)

@app.route('/showBooking')
def booking():
    result = engin.execute('SELECT * FROM info')
    show = result.fetchall()
    return render_template('showBooking.html', books=show)

@app.route('/editBooking/<Id>', methods=['POST', 'GET'])
def editHere(Id):
    print(Id)
    if request.method=='POST':
        dat = request.form.get('date')
        opts = request.form.get('opt')
        nm = request.form.get('on')
        nums = request.form.get('num')
        updateData = (dat, opts, nm, nums, Id)
        if dat=='' and nm=='' and nums =='':
            return 'Fill all forms'
        else:
            updateQuery = "UPDATE info SET dated=?, Option=?, name=?, number=? where Id=?"
            engin.execute(updateQuery,(updateData))

            return redirect('/')
    else:
        return render_template('set_edit.html')
    
@app.route('/deleteBooking/<Id>', methods=['POST', 'GET'])
def deleteHere(Id):
    print(Id)
    delQuery = "delete from info where id=?"
    engin.execute(delQuery, Id)

    return redirect('/showBooking')

@app.route('/eve', methods=["POST"])
def eve():
    dat = request.form.get('date')
    opts = request.form.get('opt')
    nm = request.form.get('on')
    nums = request.form.get('num')
    if dat=='' and nums== '' and nm=='':
        return redirect('/event')
    else:
        query = db.insert(data).values( dated=dat, option= opts, name= nm, number= nums)
        engin.execute(query)

        return redirect('/')
    
    return redirect('/event')

metadata.create_all(engin)