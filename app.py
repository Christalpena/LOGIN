from math import gamma
from multiprocessing import connection
from socketserver import DatagramRequestHandler
import sqlite3
from unicodedata import name
from flask import Flask, flash, render_template, request
import time

"""connection = sqlite3.connect("user.db")
cursor = connection.cursor()

cursor.execute("INSERT INTO users VALUES ('Christal','Perez', 'christalperez0@gmail.com','christal456')")

connection.commit()"""

#comienzan las rutas

app= Flask (__name__)
app.secret_key ='password'

connection = sqlite3.connect('user.db', check_same_thread=False)  
cursor = connection.cursor() 

@app.route('/')
def seccion():
   return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    user = request.form['username']
    password = request.form['userpassword']

    data = cursor.execute(f'SELECT password FROM users WHERE name="{user}"')
    userdata = data.fetchall()

    person = cursor.execute(f'SELECT  name  FROM users')
    dataperson = person.fetchall()

    for i in userdata:
        for data in i:
            if data == password:
                return render_template('page.html')
        break 

    for h in dataperson:
        for person in h:
            if person != user or data != password:
               flash('YOUR USERNAME OR PASSWORD IS INCORRECT', 'danger')
        break
    return render_template('index.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/signup', methods=['POST'])
def signup():

    user = request.form['name']
    last_name = request.form['Last name']
    gmail= request.form['gmail']
    password = request.form['password']

    information = user,last_name,gmail,password

    userBase = cursor.execute('SELECT name FROM users')
    dateUser = userBase.fetchall()
    
    correoBase = cursor.execute('SELECT gmail FROM users')
    dateCorreo = correoBase.fetchall()
    
    value1 = False
    value2 = 'True'
    for x in dateUser:
        for y in x:
            if y == user:
                value1 = True
                value2 = 'False'
                if value2 == 'False':
                    flash('THE USERNAME ALREADY EXISTS', 'danger')
        
        if value1 == True:
            break
    if value1 == False:
        value3 = False
        for i in dateCorreo:
            for z in i:
                if z == gmail:
                    value3 = True
                    flash('THE GMAIL ALREADY EXISTS', 'danger')
            
            if value3 == True:
                break
        if value3 == False:
            flash('REGISTERED SUCCESSFULLY!', 'success')
            cursor.execute('INSERT into users(name, last_name, gmail, password) VALUES(?, ?, ?, ?)', information)
            connection.commit()
            time.sleep(2)
            return render_template('index.html')

                            
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)








   
  