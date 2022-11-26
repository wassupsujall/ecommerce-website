

from ctypes import c_ssize_t
from pydoc import render_doc
from re import M, template

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template , request , redirect, url_for, session, Response
from datetime import datetime
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re



app = Flask(__name__)
app.secret_key= 'your secret key'
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'giftzone'
app.config["MYSQL_CURSORCLASS"]=""
mysql= MySQL(app)


@app.route("/min", methods= ['GET', 'POST'])
def mini():
    return render_template('foundpage.html')



@app.route("/important")
def imp():
       return render_template('mainpage.html')

@app.route("/shoes")
def viewp():
    return render_template('shoes.html')

@app.route("/headphone")
def headphone():
    return render_template('headphone.html')

@app.route("/per")
def perfume():
    return render_template('per.html')

@app.route("/tshirt")
def index():
    return render_template('tshirt.html')

@app.route("/hdetails"  , methods= ['GET', 'POST'])
def hdetails():
    global data
    msg = ''
    if request.method== 'POST' and 'pcolour' in request.form and 'pquantity' in request.form and 'name' in request.form and 'email' in request.form and 'phone' in request.form and 'address' in request.form and 'pincode' in request.form:
        pcolour= request.form['pcolour']
        pquantity= request.form['pquantity']
        name= request.form['name'] 
        email= request.form['email']
        phone= request.form['phone']
        address= request.form['address']
        pincode= request.form['pincode']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        '''cursor.execute('SELECT * FROM lost WHERE first_name = % s, srno = %s, relation =  %s, last_name = %s, age = %s, identity_mark = %s, date_lost= %s, address = %s, pincode = %s, city = %s, phone_num = %s, email= %s',(first_name, srno, relation, last_name, age, identity_mark, date_lost, address, pincode, city, phone_num, email) )'''
        cursor.execute('SELECT * FROM fdetails WHERE name = % s', (name,))
        lol= cursor.fetchone()
        if lol:
            msg= 'Entry already exists !'
        elif not re.match(r'[A-Za-z0-9]+', pcolour):
            msg= 'Invalid size'
        elif not re.match(r'[A-Za-z0-9]+', pquantity):
            msg= 'Invalid quantity'
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg= 'Invalid name'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg= 'Invalid email'
        elif not re.match(r'[A-Za-z0-9]+', phone):
            msg= 'Invalid phone'
        elif not re.match(r'[A-Za-z0-9]+', address):
            msg= 'Invalid address'
        elif not re.match(r'[A-Za-z0-9]+', pincode):
            msg= 'Invalid pincode'
       
        else:
            cursor.execute('INSERT INTO fdetails VALUES ( %s, %s, %s, %s, %s, %s, %s)', (pcolour, pquantity, name, email, phone, address, pincode, ))
            mysql.connection.commit()
            msg= 'Succesfully entered the data'
    elif request.method == 'POST':
        msg= 'Please fill out form'
    
    return render_template('hdetails.html', msg=msg)




@app.route("/contact" , methods= ['GET', 'POST'])
def contact():
    global data
    msg = ''
    if request.method== 'POST' and 'name' in request.form and 'email' in request.form and 'phone' in request.form and 'msg' in request.form: 
        name= request.form['name'] 
        email= request.form['email']
        phone= request.form['phone']
        msg= request.form['msg'] 
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM contacts WHERE name = % s', (name,))
        contact= cursor.fetchone()
        if contact:
            msg= 'Entry already exists !'
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg= 'Invalid name'
       
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg= 'Invalid email'
        elif not re.match(r'[A-Za-z0-9]+', phone):
            msg= 'Invalid locatin'
        elif not re.match(r'[A-Za-z0-9]+', msg):
            msg= 'Invalid data'
        else:
            cursor.execute('INSERT INTO contacts VALUES ( %s, %s, %s, %s)', (name, email, phone, msg, ))
            mysql.connection.commit()
            msg= 'Succesfully entered the data'
    elif request.method == 'POST':
        msg= 'Please fill out form'
    return render_template('index.html', msg=msg)

@app.route("/details", methods= ['GET', 'POST'])
def details():
    global data
    msg = ''
    if request.method== 'POST' and 'psize' in request.form and 'pquantity' in request.form and 'name' in request.form and 'email' in request.form and 'phone' in request.form and 'address' in request.form and 'pincode' in request.form:
        psize= request.form['psize']
        pquantity= request.form['pquantity']
        name= request.form['name'] 
        email= request.form['email']
        phone= request.form['phone']
        address= request.form['address']
        pincode= request.form['pincode']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        '''cursor.execute('SELECT * FROM lost WHERE first_name = % s, srno = %s, relation =  %s, last_name = %s, age = %s, identity_mark = %s, date_lost= %s, address = %s, pincode = %s, city = %s, phone_num = %s, email= %s',(first_name, srno, relation, last_name, age, identity_mark, date_lost, address, pincode, city, phone_num, email) )'''
        cursor.execute('SELECT * FROM details WHERE name = % s', (name,))
        lol= cursor.fetchone()
        if lol:
            msg= 'Entry already exists !'
        elif not re.match(r'[A-Za-z0-9]+', psize):
            msg= 'Invalid size'
        elif not re.match(r'[A-Za-z0-9]+', pquantity):
            msg= 'Invalid quantity'
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg= 'Invalid name'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg= 'Invalid email'
        elif not re.match(r'[A-Za-z0-9]+', phone):
            msg= 'Invalid phone'
        elif not re.match(r'[A-Za-z0-9]+', address):
            msg= 'Invalid address'
        elif not re.match(r'[A-Za-z0-9]+', pincode):
            msg= 'Invalid pincode'
       
        else:
            cursor.execute('INSERT INTO details VALUES ( %s, %s, %s, %s, %s, %s, %s)', (psize, pquantity, name, email, phone, address, pincode, ))
            mysql.connection.commit()
            msg= 'Succesfully entered the data'
    elif request.method == 'POST':
        msg= 'Please fill out form'
    return render_template('details.html', msg=msg)
app.run(debug=True)

@app.route("/hdetails")
def hdetails():
    return render_template('hdetails.html')













@app.route("/mp")
def mp():
    return render_template('view.html' )
app.run(debug=True) 


@app.route("/major", methods= ['GET', 'POST'])
def major():    
    global data
    msg = ''
    if request.method== 'POST' and 'srno' in request.form and 'relation' in request.form and 'first_name' in request.form and 'last_name' in request.form and 'age' in request.form and 'identity_mark' in request.form and 'date_lost' in request.form and 'address' in request.form and 'pincode' in request.form and 'city' in request.form and 'phone_num' in request.form and 'email' in request.form:
        srno= request.form['srno']
        relation= request.form['relation']
        first_name= request.form['first_name'] 
        last_name= request.form['last_name']
        age= request.form['age']
        identity_mark= request.form['identity_mark']
        date_lost= request.form['date_lost']
        address= request.form['address']
        pincode= request.form['pincode']
        city= request.form['city'] 
        phone_num= request.form['phone_num'] 
        email= request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        '''cursor.execute('SELECT * FROM lost WHERE first_name = % s, srno = %s, relation =  %s, last_name = %s, age = %s, identity_mark = %s, date_lost= %s, address = %s, pincode = %s, city = %s, phone_num = %s, email= %s',(first_name, srno, relation, last_name, age, identity_mark, date_lost, address, pincode, city, phone_num, email) )'''
        cursor.execute('SELECT * FROM lost WHERE first_name = % s', (first_name,))
        lol= cursor.fetchone()
        if lol:
            msg= 'Entry already exists !'
        elif not re.match(r'[A-Za-z0-9]+', srno):
            msg= 'Invalid name'
        elif not re.match(r'[A-Za-z0-9]+', relation):
            msg= 'Invalid relation'
        elif not re.match(r'[A-Za-z0-9]+', first_name):
            msg= 'Invalid name'
        elif not re.match(r'[A-Za-z0-9]+', last_name):
            msg= 'Invalid name'
        elif not re.match(r'[A-Za-z0-9]+', age):
            msg= 'Invalid age'
        elif not re.match(r'[A-Za-z0-9]+', identity_mark):
            msg= 'Invalid identity mark'
        elif not re.match(r'[A-Za-z0-9]+', date_lost):
            msg= 'Invalid date'
        elif not re.match(r'[A-Za-z0-9]+', address):
            msg= 'Invalid address'
        elif not re.match(r'[A-Za-z0-9]+', pincode):
            msg= 'Invalid pincode'
        elif not re.match(r'[A-Za-z0-9]+', city):
            msg= 'Invalid city'
        elif not re.match(r'[A-Za-z0-9]+', phone_num):
            msg= 'Invalid number'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg= 'Invalid email'
        
        else:
            cursor.execute('INSERT INTO lost VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (srno, relation, first_name, last_name, age, identity_mark, date_lost,  address, pincode, city,phone_num,  email, ))
            mysql.connection.commit()
            msg= 'Succesfully entered the data'
    elif request.method == 'POST':
        msg= 'Please fill out form'
    return render_template('adminlogin.html', msg= msg)
       