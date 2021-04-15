from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
# import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('users_schema')
    # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM users;')  # call the query_db function, pass in the query as a string
    return render_template("display.html", friends = friends)

@app.route("/form")
def form():
    return render_template("read.html")

@app.route("/delete_friend/<user_num>")
def delete(user_num):
    mysql = connectToMySQL('users_schema')
    query = 'DELETE FROM users WHERE id = %(user_num)s;'
    data = {
        "user_num": user_num
    }
    users = mysql.query_db(query,data)
    print(users)
    return redirect("/")

@app.route("/show_person/<int:id>")
def person(id):
    mysql = connectToMySQL('users_schema')
    query = 'SELECT * FROM users WHERE id = %(id)s;'
    data = {
        "id": id
    }
    users = mysql.query_db(query,data)
    return render_template("individual.html", user = users[0])

@app.route("/edit/<int:id>")
def edit(id):
    mysql = connectToMySQL('users_schema')
    query = 'SELECT * FROM users WHERE id = %(id)s;'
    data = {
        "id": id
    }
    users = mysql.query_db(query,data)
    return render_template("edit.html", user = users[0])

@app.route("/edit_person/<int:id>", methods = ["POST"])
def edit_person(id):
    mysql = connectToMySQL('users_schema')
    query = 'UPDATE users SET first_name = %(fn)s,last_name = %(ln)s,email = %(em)s WHERE id = %(id)s;'
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"],
        "id": id
    }
    mysql.query_db(query,data)
    return redirect("/")

@app.route("/create_friend", methods = ["POST"])
def add_friend_to_db():
    mysql = connectToMySQL('users_schema')
    query = 'INSERT INTO users(first_name,last_name,email,created_at,updated_at) VALUES(%(fn)s, %(ln)s, %(em)s, NOW(), NOW());'
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"]
    }
    new_user_id = mysql.query_db(query,data)
    print(new_user_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)