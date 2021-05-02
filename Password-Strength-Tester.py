#My main file for code

from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    inputName = request.form['myName']

    #split password given into list, separated by commas, and set var for password score
    inputName.split(",")
    strength_score = 0
    
    #gathers points based on what the password is comprised of, character wise
    for character in inputName:
        if character.isalpha():
            if character.isupper():
                strength_score += 2
            else:   
                strength_score += 1
        elif character.isdigit():
            strength_score += 2
        else:
            strength_score += 6

    #gathers points based on how long password is
    if len(inputName) < 5:
        strength_score += 3
    elif len(inputName) >= 5 and len(inputName) < 8:
        strength_score += 6
    elif len(inputName) >= 8 and len(inputName) < 11:
        strength_score += 9
    else:
        strength_score += 12

    #gathers score for password based on points collected
    if strength_score < 15:
        final_score = "Insufficent..."
    elif strength_score >=15 and strength_score < 25:
        final_score = "Sufficent."
    else:
        final_score = "Excellent!"
    
    #prints password given, points score, and final score word
    inputName ="\'" + inputName + "\' is the password you inputted, and it has \na strength of " + str(strength_score) + "! " + final_score
    return render_template("home.html",myName=inputName)

@app.route('/') 
def home():
    return render_template("home.html",myName="")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
    
