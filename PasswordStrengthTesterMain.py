#My main file for code
from flask import Flask, render_template, request app=Flask(__name__)
@app.route('/greet',methods=['POST'])

@app.route('/')
def home():
   return render_template("home.html",myName="")
  
@app.route('/about/')
def about():
  return render_template("about.html")

if __name__=="__main__":
  app.run(debug=True)
  
@app.route('/greet',methods=['POST'])
def passtest():
  inputPass = request.form[myPass']
  ip = request.remote_addr
  inputPass = inputPass.upper()+" is the password inputted from " + str(ip)
  return render_template("home.html",myPass=inputPass)
