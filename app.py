import json

import MySQLdb
import sqlweb

from ECC_encryption import *
from listElementToBytes import *
from key_generation import *
from CSV_management import *
from Mysql_Conneection_chehck import *
from flask import Flask, request, url_for, redirect, render_template, flash, session, g ,jsonify, send_file
import pickle
from werkzeug.utils import secure_filename
import os
import pandas as pd
from tinyec import registry
from Crypto.Cipher import AES
import hashlib, secrets, binascii
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'data/Client/Uploaded_file'
ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(20)

# Configure Db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Gokul@123'
app.config['MYSQL_DB'] = 'sensor_data'
mysql = MySQL(app)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/client')
def client_main():
    return render_template("client.html")


@app.route('/admin')
def admin_main():
    session.pop("admin", None)
    return render_template("Admin.html")


@app.route("/admin_login_done",methods=['GET', 'POST'])
def admin_login_done():
    if request.method == 'POST':
        session.pop("admin", None)
        k = request.form
        email = k['email']
        password = k['password']
        if email == "admin123@gmail.com" and password == "root@123":
            session['admin'] = email
            flash("successfully Logged in")
            return redirect(url_for('protected_admin'))
        else:
            flash("Incorrect username or password")
            return render_template("Admin.html")


@app.route('/client_signup')
def client_signup():
    return render_template("Client_Signup.html")


@app.route('/client_signup_done', methods=['GET', 'POST'])
def client_signup_done():
    if request.method == 'POST':
        k = request.form
        username = k['name']
        password = k['pass1']
        confirm_pass = k['pass2']
        email = k['email']
        if (password != confirm_pass):
            flash("passwords are not same!!")
            return render_template("Client_Signup.html")
        cur = mysql.connection.cursor()
        list1 = [email, username, password]
        try:
            cur.execute("INSERT INTO client_signup(Email, username, password) VALUES(%s, %s, %s)", list1)
            mysql.connection.commit()
            print(cur.rowcount, "record inserted.")
            cur.close()
            return ("Signup Succeess")
        except mysql.connection.IntegrityError:
            flash("Account already exits ")
            return redirect("/client_signup")


@app.route('/client_login')
def client_login():
    session.pop("user", None)
    return render_template("Client_Login.html")


@app.route("/client_login_done", methods=['GET', 'POST'])
def client_login_done():
    if request.method == 'POST':
        session.pop("user", None)
        k = request.form
        email = k['email']
        password = k['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM client_signup WHERE email= %s AND password= %s", (email, password))
        account = cur.fetchone()
        if account:
            session['user'] = email
            flash("successfully Logged in")
            return redirect(url_for('protected'))
        else:
            flash("Incorrect username or password")
            return render_template("Client_Login.html")


@app.route('/protected')
def protected():
    if g.user:
        return render_template("protected.html", user=session['user'])
    return redirect('/client_login')


@app.route('/encrypt', methods=['GET', 'POST'])
def encrypted():
    if g.user:
        if request.method == "POST":
            if request.files['file'].filename == '':
                flash("Please select a file")
                return render_template("protected.html", user=session['user'])
            try:
                user = session['user']
                list1=user.split('@')
                path1 = "Keys/" + list1[0] + "/public.dictionary"
                pri = open(path1, 'r')
                pri.close()
            except FileNotFoundError:
                flash("Keys are not available in your local storage. Create New Ecc Keys")
                return render_template("protected.html", user=session['user'])
            file = request.files['file']
            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename1 = session['user'] + '.csv'
                k = "data/Client/Uploaded_file/" + filename1
                # filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
                pub = open(path1, 'rb')
                pub1 = pickle.load(pub)
                pubkey = pub1['value']
                path_encry_csv = "data/Client/Encrypted_files/" + filename1
                list2 = CSV_to_encrycsv(k, pubkey, path_encry_csv)
                index = list2[-1]
                list2.pop(-1)
                table_name = session['user']
                k2 = table_name.split('@')
                table_name = k2[0]
                cur = mysql.connection.cursor()
                ok1 = Mysql_table_query(table_name, index)
                sql = ok1[0]
                index = ok1[-1]
                try:
                    cur.execute(sql)
                    ok2 = Mysql_column_query(index)
                    index = ok2[0]
                    column = ok2[-1]
                    sql2 = "INSERT INTO " + table_name + index + " " + column
                    print(sql2)
                    for i in range(len(list2)):
                        values = ListElementToBytes(list2[i])
                        cur.execute(sql2, values)
                        mysql.connection.commit()
                    print(cur.rowcount, "record inserted.")
                    flash("Successfully encrypted and uploaded to Database")
                    return render_template("protected.html", user=session['user'])
                except MySQLdb.OperationalError:
                    flash("Table already exits")
                    return render_template("protected.html", user=session['user'])
            else:
                flash("please provide only csv file")
                return render_template("protected.html", user=session['user'])
        else:
            return redirect('/protected')
    flash("Loggedout unexpectedly")
    return redirect('/client_login')  


@app.before_request
def before_request():
    g.admin= None
    g.user = None
    if 'user' in session:
        g.user = session['user']
    elif 'admin' in session:
        g.admin = session['admin']

@app.route("/drop_session")
def drop_session():
    session.pop('user', None)
    flash("logged out successfully")
    return redirect("client_login")

@app.route("/drop_session_admin")
def drop_session_admin():
    session.pop('admin', None)
    flash("logged out successfully")
    return redirect("admin")


@app.route("/generate_keys")
def generate_keys():
    if g.user:
        try:
            user = session['user']
            list1=user.split('@')
            user1=list1[0]
            path1 = "Keys/" + user1 + "/private.txt"
            pri = open(path1, 'r')
            pri.close()
        except FileNotFoundError:
            key_gen_user(user1)
            flash("Key generated Successfully")
            return render_template("protected.html", user=session['user'])
        flash("Keys are available no need to create new one")
        return render_template("protected.html", user=session['user'])
    else:
        flash("logged out Unexpectedly")
        return redirect('/client_login')


@app.route('/protected_admin')
def protected_admin():
    if g.admin:
        return render_template("protected_admin.html", admin=session['admin'],user="ADMIN")
    return redirect('/admin')

@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    if g.admin:
        search_word =' '
        cur = mysql.connection.cursor()
        if request.method == 'POST':
            search_word = request.form['query']
            if search_word == ' ':
                query = "Show tables"
                cur.execute(query)
                numrows = int(cur.rowcount)
                employee = cur.fetchall() 
                return jsonify({'htmlresponse': render_template('response.html', employee=employee, numrows=numrows,k="All_Records")})
            else:    
                query = "SHOW TABLES LIKE '%{}%'".format(search_word)
                cur.execute(query)
                numrows = int(cur.rowcount)
                employee = cur.fetchall()
                return jsonify({'htmlresponse': render_template('response.html', employee=employee, numrows=numrows)})
    else:
        flash("logged out Unexpectedly")
        return redirect('/admin')

@app.route("/load_data",methods=["POST","GET"])
def load_data():
    cur = mysql.connection.cursor()
    if g.admin:
        if request.method == 'POST':
            table_name = request.form
            username = table_name['table_name']
            query = "Show tables"
            cur.execute(query)
            employee = cur.fetchall() 
            list2=[]
            for i in employee:
                list2.append(i[0])
            if(username in list2):
                return render_template('load_data.html',user=username)
            else:
                flash("No data is available assosiated with given username")
                return render_template('protected_admin.html',user="ADMIN")

    else:
        flash("logged out Unexpectedly")
        return render_template("Admin.html")
@app.route("/Get_encrypted_data",methods=["POST","GET"])
def Get_encrypted_data():
    if g.admin:
        cur = mysql.connection.cursor()
        username=request.args.get("user1")
        query1="SHOW COLUMNS FROM "+username
        cur.execute(query1)
        index=cur.fetchall()
        index1=[]
        for i in index:
            index1.append(i[0])
        query="SELECT * FROM "+username
        cur.execute(query)
        user_data=cur.fetchall()
        print(type(user_data))
        k = "data/Admin/Encrypted_files/" +username+".csv"
        list_to_csv(k,user_data,index1)
        return send_file(k, as_attachment=True)
    else:
        flash("logged out Unexpectedly")
        return redirect('/admin')
@app.route("/Get_decrypted_data",methods=["POST","GET"])
def Get_decrypted_data():
    if g.admin:
        cur = mysql.connection.cursor()
        username=request.args.get("user1")
        query1="SHOW COLUMNS FROM "+username
        cur.execute(query1)
        index=cur.fetchall()
        index1=[]
        for i in index:
            index1.append(i[0])
        query="SELECT * FROM "+username
        cur.execute(query)
        user_data=cur.fetchall()
        priv_key=open("Keys/"+username+"/private.txt",'r')
        pri1=int(priv_key.read())
        k = "data/Admin/Decrypted_files/" +username+".csv"
        list2=[]
        for i in user_data:
            list2.append(list(i))
        CSV_to_decrycsv(list2,index1,pri1,k)
        return send_file(k, as_attachment=True)
    else:
        flash("logged out Unexpectedly")
        return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
