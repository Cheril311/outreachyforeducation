from flask import Flask, render_template, request
import sqlite3 as sql
import smtplib, ssl
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')
@app.route('/outreach')
def outreach():
    return render_template('outreach.html')

@app.route('/donate')
def donate():
   return render_template('form.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         email = request.form['email']
         city = request.form['city']
         amount = request.form['amount']
         
         with sql.connect("donorinfo.db") as con:
            cur = con.cursor()
            
            cur.execute('''INSERT INTO students (name,email,city,amount) 
               VALUES (?,?,?,?)''',(nm,email,city,amount) )
            
            con.commit()
            msg = "Record successfully added, please check your email"
            
            message = "Thankyou for your generous donation of Rs." + amount
            context=ssl.create_default_context()
            server = smtplib.SMTP("smtp.gmail.com" , 587)
            server.starttls(context = context)
            server.login("outreachyforchildren@gmail.com" , "outreachy.com")
            server.sendmail("outreachyforchildren@gmail.com" , email, message)
            
         
            
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()
     

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)



if __name__ == '__main__':
   app.run(debug = True)