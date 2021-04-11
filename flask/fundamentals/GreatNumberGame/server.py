from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Keep_it_secret_keep-It-safe"

@app.route("/")
def base():
    session['num'] = random.randint(0,100)
    return render_template("html.html")

@app.route("/main",methods = ['POST'])
def main():
    guess = request.form['guess']
    if(int(guess) > int(session['num'])):
        value = "wrong.html"
    if(int(guess) < int(session['num'])):
        value = "right.html"
    if(int(guess) == int(session['num'])):
        value = "win.html"
    return render_template(value)

@app.route("/wrong", methods = ['POST'])
def wrongGuess():
    guess = request.form['guess']
    if(int(guess) > int(session['num'])):
        value = "wrong.html"
    if(int(guess) < int(session['num'])):
        value = "right.html"
    if(int(guess) == int(session['num'])):
        value = "win.html"
    return render_template(value)

@app.route("/right", methods = ['POST'])
def rightGuess():
    guess = request.form['guess']
    if(int(guess) > int(session['num'])):
        value = "wrong.html"
    if(int(guess) < int(session['num'])):
        value = "right.html"
    if(int(guess) == int(session['num'])):
        value = "win.html"
    return render_template(value)

if __name__ == "__main__":
    app.run(debug=True)

    ##only use two route fooo