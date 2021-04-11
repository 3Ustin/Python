from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route("/")
def route():
    if 'name' not in session:
        session['name'] = 1
    else:
        session['name'] +=1
    return render_template("html.html")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)