from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("html.html")
    
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name0 = request.form['name0']
    last0 = request.form['last0']
    name1 = request.form['name1']
    last1 = request.form['last1']
    name2 = request.form['name2']
    last2 = request.form['last2']
    name3 = request.form['name3']
    last3 = request.form['last3']
    return render_template("show.html", name0 = name0, name1 = name1,name2 = name2,name3 = name3,last0=last0,last1=last1,last2=last2,last3=last3)


if __name__ == "__main__":
    app.run(debug=True)