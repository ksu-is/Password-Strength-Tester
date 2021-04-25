#My main file for code

from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    inputName = request.form['myName']
    
    #tester here
    strength_score = 100
    
    inputName ="\'" + inputName + "\' is the password you inputted, and it has a strength of " + str(strength_score) + " out of 100!"
    return render_template("home.html",myName=inputName)

@app.route('/')
def home():
    return render_template("home.html",myName="")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
