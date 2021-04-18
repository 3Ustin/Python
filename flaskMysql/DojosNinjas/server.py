from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
# import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('dojos_ninjas_schema')
    # call the function, passing in the name of our db
    dojoDisplay = mysql.query_db('SELECT * FROM dojos;')
    # call the query_db function, pass in the query as a string
    return render_template("Home.html", dojos = dojoDisplay)

@app.route("/add_dojo", methods = ["POST"])
def addDojo():
    mysql = connectToMySQL('dojos_ninjas_schema')
    query = 'INSERT INTO dojos(name,created_at,updated_at) VALUES(%(fn)s,NOW(), NOW());'
    data = {
        "fn": request.form["fname"]
    }
    mysql.query_db(query,data)
    return redirect("/")

@app.route("/show_dojo/<int:id>")
def person(id):
    mysql = connectToMySQL('dojos_ninjas_schema')
    query = "SELECT dojos.id, ninjas.id, ninjas.first_name, ninjas.age FROM ninjas JOIN dojos ON dojo_id = dojo.id WHERE dojo_id = %(id)s;"
    data = {
        "id": id
    }
    dojos = mysql.query_db(query,data)
    return render_template("dojoShow.html", dojos = dojos)

@app.route("/ninjaShow")
def add_friend_to_db():
    mysql = connectToMySQL('dojos_ninjas_schema')
    query = "SELECT * FROM dojos"
    data = {}
    dojos = mysql.query_db(query,data)
    return render_template("addNinja.html", dojos = dojos)

@app.route("/add_ninja", methods = ["POST"])
def ninjaAdd():
    mysql = connectToMySQL('dojos_ninjas_schema')
    query = 'INSERT INTO ninjas(dojo_id,first_name,last_name,age,created_at,updated_at) 
    VALUES(%(do)s,%(fn)s, %(ln)s, %(age)s, NOW(), NOW());'
    data = {
        "do": request.form["dojo"],
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "age": request.form["age"]
    }
    dojos = mysql.query_db(query,data)
    print(dojos)
    return redirect("/ninjaShow")





if __name__ == "__main__":
    app.run(debug=True)