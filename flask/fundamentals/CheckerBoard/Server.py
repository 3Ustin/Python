from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def func():
    return render_template('index.html', phrase = "hello", times = 5)

@app.route("/play/<x>/<color>")
def derel(x,color):
    return render_template('index.html', boxes = int(x),color = color)


if __name__ == "__main__":
    app.run(debug=True)