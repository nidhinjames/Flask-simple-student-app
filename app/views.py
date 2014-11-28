from flask import render_template
from flask import request
import sqlite3 as lite
from flask import flash
from app import app

@app.route('/')
@app.route('/index')
def index():
    header = {'h1': 'STUDENT DETAILS'}  # fake user
    return render_template('index.html',
                           title='Home',
                           header=header)
@app.route('/details')
def details():
        head = {'hd': 'ENTER DETAILS!!!'}
        return render_template('details.html',
                                title = 'Details',
                                head = head)        

@app.route('/insert', methods = ['GET','POST'])
def insert():
	fname = request.form['fname']
	sname = request.form['sname']
	email = request.form['email']
	sex = request.form['sex']
   
	con = lite.connect('test.db')
	
	with con:
		cur = con.cursor()
		cur.execute('insert into Student (fname,sname,email,sex) values (?,?,?,?)',[fname,sname,email,sex])
	return "data inserted"




@app.route('/display', methods = ['GET','POST'])
def display():
	head = {'h3': 'STUDENT DETAILS'}


	con = lite.connect('test.db')
	
	with con:
		cur = con.cursor()
		cursor = cur.execute("SELECT * FROM Student")
		rows = []

   	
		for row in cursor:
			rows.append(row)

		return render_template('display.html',
			       	        title = 'Display',
					head = head,	
                               		rows = rows)

                                              

@app.route('/delete', methods = ['GET','POST'])
def delete():
	 head = {'h3': 'STUDENT DETAILS'}
	 fname = request.form['fname']
        

	 con = lite.connect('test.db')
	 with con:
                cur = con.cursor()
		cur.execute("DELETE FROM Student \
			    WHERE fname =(?)",  ((request.form['fname'],)))
		rows = []
		cursor = cur.execute("SELECT * FROM Student")               
                for row in cursor:
                        rows.append(row)

                return render_template('delete.html',
                                        title = 'Display',
                                        head = head,
                                        rows = rows)
	





                       	      


                                    
