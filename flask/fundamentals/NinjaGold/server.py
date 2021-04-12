from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route("/")
def index():
    if 'gold_amount' not in session:
        session['gold_amount'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template("index.html", activities = session['activities'])
    
@app.route('/process_money', methods=['POST'])
def create_user():
    if request.form['action'] == 'farm':
        num = random.randint(10,20)
        session['gold_amount'] += num
        session['activities'].append("the Farm made you: " + str(num) + " dollars" + datetime.datetime.now().strftime("%c"))
        # THIS IS PUTTING EMBEDDING HTML INTO THE INDEX.
        #UNSOLVED SOLUTION ::
        # session['activities'].append(<div class = 'won'> + str(num) + </div>)
    elif request.form['action'] == 'woods':
        num = random.randint(5,10)
        session['gold_amount'] += num
        session['activities'].append("the Farm made you: " + str(num) + " dollars" + datetime.datetime.now().strftime("%c"))
    elif request.form['action'] == 'bank':
        num = random.randint(2,5)
        session['gold_amount'] += num
        session['activities'].append("the Farm made you: " + str(num) + " dollars" + datetime.datetime.now().strftime("%c"))
    elif request.form['action'] == 'casino':
        num = random.randint(-50,50)
        session['gold_amount'] += num
        session['activities'].append("the Farm made you: " + str(num) + " dollars" + datetime.datetime.now().strftime("%c"))
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)