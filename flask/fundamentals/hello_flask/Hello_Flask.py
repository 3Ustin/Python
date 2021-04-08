from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'

@app.route("/dojo")
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def sayHi():
    return "Hello: " + name
@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    string = ""
    for i in range(0,int(num)):
        print(word)
    return string
@app.route("/hello/<name>")
def hello(name):
    print(name)
    return"Hello, " + name

@app.route("/users/<username>/<id>")
def show_user_profile(username,id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route("/success")
def success():
    return "success"


#Adien's example.
#
# @app.route("/users")
# def users():
#     db_users = [
#         {"first_name":'Austin',"Last_name":'Dupras'}
#         {"first_name":'Preston',"Davis":'Dupras'}
#         {"Harleigh":'Austin',"McLellan":'Dupras'}
#     ]
#     return render_template("users.html",users = db_users)


if __name__=="__main__":
    #starting server
    # we ask to debug
    app.run(debug=True)