from flask import Flask, render_template, redirect, request,flash, session
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

# import the function that will return an instance of a connection
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "keep it secret, keep it safe"
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# This route 
@app.route("/")
def login_registeration():
    return render_template("login_register.html")


@app.route("/login", methods = ["POST"])
def loginChecking():
    # starting with true assumption, then proceeding to check that assumption. 
    is_Valid = True
    if len(request.form['email']) < 1:
        is_Valid = False
    if not EMAIL_REGEX.match(str(request.form['email'])):
        is_Valid = False
    if len(request.form['password']) < 1:
        is_Valid = False

    #If NOT all tests fail, reroute back to origin, and claim error.
    if not is_Valid:
        flash("Login values missing.")
        return redirect("/")
    #the rest of our code for a succsessfull validation goes here.
    else:
        #This is dedicated space for the login process.
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL('exam')
        query = 'SELECT * from users;'
        isRegistered = mysql.query_db(query)
        for register in isRegistered:
            if register['email'] == request.form['email'] and bcrypt.check_password_hash(register['password'],request.form['password']):
                session['user_id'] = register['id']
                return redirect("/dashboard")
        return redirect("/")


@app.route("/register", methods = ["POST"])
def registerChecking():
    # starting with true assumption, then proceeding to check that assumption. 
    is_Valid = True
    if len(request.form['firstname']) < 1:
        is_Valid = False
    if len(request.form['lastname']) < 1:
        is_Valid = False
    if len(request.form['password']) < 1:
        is_Valid = False
    if not EMAIL_REGEX.match(str(request.form['email'])):
        is_Valid = False
    if len(request.form['email']) < 1:
        is_Valid = False
    if request.form['password'] != request.form['confirmPassword']:
        is_Valid = False

    #If NOT all tests fail, reroute back to origin, and claim error.
    if not is_Valid:
        flash("registration values missing.")
        return redirect("/")
    #the rest of our code for a succsessfull validation goes here.
    else:
        #This is dedicated space for the login process.
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL('exam')
        query = 'INSERT INTO users (email, password, firstname, lastname, created_at, updated_at) VALUES (%(email)s,%(password_hash)s, %(firstname)s, %(lastname)s,NOW(),NOW());'
        data = {
            "email" : request.form['email'],
            "firstname" : request.form['firstname'],
            "lastname" : request.form['lastname'],
            "password_hash" : pw_hash
        }
        isRegistered = mysql.query_db(query,data)
        
        return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    #query to grab champion_id to bring to other html doc.
    mysql = connectToMySQL('exam')
    query = 'SELECT users.firstname, users.lastname, title, magazines.id FROM magazines JOIN users ON user_id = users.id;'
    magazines = mysql.query_db(query)
    mysql = connectToMySQL('exam')
    query = 'SELECT * FROM users WHERE id = %(user_id)s;'
    data = {
        "user_id" : session['user_id']
    }
    users = mysql.query_db(query,data)
    return render_template("dashboard.html", magazines = magazines,users=users[0])

@app.route("/dashboard/subscribe/<mag_id>")
def dashboardSubscribe(mag_id):
    mysql = connectToMySQL('exam')
    query = 'INSERT INTO subscriptions (user_id, magazine_id) VALUES (%(user_id)s,%(mag_id)s);'
    data = {
        "user_id" : session['user_id'],
        "mag_id" : mag_id
    }
    result = mysql.query_db(query,data)

    mysql = connectToMySQL('exam')
    query = 'SELECT subs FROM magazines WHERE id = %(mag_id)s;'
    data = {
        "mag_id" : mag_id
    }
    subList= mysql.query_db(query,data)
    subList[0]['subs'] = subList[0]["subs"] + 1


    mysql = connectToMySQL('exam')
    query = 'UPDATE magazines SET subs = %(subs)s WHERE id = %(mag_id)s;'
    data = {
        "subs" : subList[0]['subs'],
        "mag_id" : mag_id
    }
    result = mysql.query_db(query,data)

    return redirect("/dashboard")

@app.route("/magazines/<id>/<firstname>/<lastname>")
def magazine(id,firstname,lastname):
    mysql = connectToMySQL('exam')
    query = 'SELECT * FROM magazines WHERE id = %(id)s;'
    data = {
        "id" : id
    }
    magazine = mysql.query_db(query,data)

    mysql = connectToMySQL('exam')
    query = 'SELECT subscriptions.user_id, subscriptions.magazine_id, firstname, lastname FROM subscriptions JOIN users ON user_id = users.id JOIN magazines ON magazine_id = magazines.id WHERE subscriptions.magazine_id = %(id)s;'
    data = {
        "id" : id
    }

    subs = mysql.query_db(query,data)
    print(subs)
    return render_template("magazines.html",magazine = magazine[0],firstname = firstname,lastname = lastname,subs = subs)

@app.route("/magazine_add")
def magazine_add():
    return render_template("magazine_add.html")

@app.route("/magazine_add/checking", methods = ["POST"])
def magazine_add_checking():
    is_Valid = True
    if len(request.form['title']) < 1:
        is_Valid = False
    if len(request.form['description']) < 1:
        is_Valid = False

    #If NOT all tests fail, reroute back to origin, and claim error.
    if not is_Valid:
        flash("Magazine information missing.")
        return redirect("/magazine_add")
    #the rest of our code for a succsessfull validation goes here.
    else:
        #This is dedicated space for the login process.
        mysql = connectToMySQL('exam')
        query = 'INSERT INTO magazines (title, description,created_at, updated_at, user_id,subs) VALUES (%(title)s,%(description)s,NOW(),NOW(), %(user_id)s,0);'
        data = {
            "title" : request.form['title'],
            "description" : request.form['description'],
            "user_id" : session['user_id'],
        }
        isRegistered = mysql.query_db(query,data)
        
        return redirect("/dashboard")

@app.route("/userPage")
def userPage():
    mysql = connectToMySQL('exam')
    query = 'SELECT * FROM magazines WHERE user_id = %(user_id)s;'
    data = {
        "user_id" : session['user_id']
    }
    magazines = mysql.query_db(query,data)

    mysql = connectToMySQL('exam')
    query = 'SELECT * FROM users WHERE id = %(user_id)s;'
    data = {
        "user_id" : session['user_id']
    }
    users = mysql.query_db(query,data)
    i = 0
    mysql = connectToMySQL('exam')
    query = 'SELECT * FROM subscriptions;'
    subs = mysql.query_db(query)
    return render_template('userPage.html', magazines = magazines,user = users[0],subs = subs, i = i)

@app.route("/userPage/updating", methods = ["POST"])
def userPage_updating():
    is_Valid = True
    if len(request.form['firstname']) < 1:
        is_Valid = False
    if len(request.form['lastname']) < 1:
        is_Valid = False
    if not EMAIL_REGEX.match(str(request.form['email'])):
        is_Valid = False
    if len(request.form['email']) < 1:
        is_Valid = False

    #If NOT all tests fail, reroute back to origin, and claim error.
    if not is_Valid:
        flash("User Update information missing.")
        return redirect("/userPage")
    #the rest of our code for a succsessfull validation goes here.
    else:
        #This is dedicated space for the login process.
        mysql = connectToMySQL('exam')
        query = 'UPDATE users SET email = %(email)s, firstname = %(firstname)s, lastname = %(lastname)s, updated_at = NOW() WHERE id = %(id)s;' 
        data = {
            "firstname" : request.form['firstname'],
            "lastname" : request.form['lastname'],
            "email" : request.form['email'],
            "id" : session['user_id']
        }
        isRegistered = mysql.query_db(query,data)
        
        return redirect("/userPage")

@app.route("/userPage/deleteMagazine/<mag_id>")
def userPage_deletingMagazine(mag_id):
    mysql = connectToMySQL('exam')
    query = 'DELETE FROM magazines WHERE id = %(id)s;'
    data = {
        "id" : mag_id
    }
    mysql.query_db(query,data)
    return redirect("/userPage")



# @app.route("/champion/", methods = ["POST"])
# def submittedChampionForm():
#     # starting with true assumption, then proceeding to check that assumption. 
#     is_Valid = True
#     if len(request.form['champion']) < 1:
#         is_Valid = False
#     if len(request.form['role_id']) < 1:
#         is_Valid = False
#     if len(request.form['category_id']) < 1:
#         is_Valid = False
#     if len(request.form['timesPlayed']) < 1:
#         is_Valid = False
#     if len(request.form['ReasonIPlay']) < 1:
#         is_Valid = False

#     #If NOT all tests fail, reroute back to origin, and claim error.
#     if not is_Valid:
#         flash("Champion values missing.")
#         return redirect("/")
#     #the rest of our code for a succsessfull validation goes here.
#     else:
#         #Quering the database, inserting the posted champion. 
#         mysql = connectToMySQL('leaguechampionlog')
#         query = 'INSERT INTO champions(Champion,roles_id, timesPlayed, categories_id, ReasonIPlay, created_at, updated_at) VALUE(%(champion)s, %(role)s, %(timesPlayed)s, %(category)s, %(ReasonIPlay)s, NOW(), NOW());'
#         data = {
#             "champion": request.form["champion"],
#             "role": request.form["role_id"],
#             "timesPlayed": request.form["timesPlayed"],
#             "category": request.form["category_id"],
#             "ReasonIPlay": request.form["ReasonIPlay"]
#         }
#         champion_id = mysql.query_db(query,data)
#         return redirect(f"/champion/show/{champion_id}")

# @app.route("/champion/show/<champion_id>")
# def showingSubmittedChampionForm(champion_id):
#     #query to grab champion_id to bring to other html doc.
#     mysql = connectToMySQL('leaguechampionlog')
#     query = 'SELECT Champion, categories.name, roles.name, timesPlayed, ReasonIPlay FROM champions JOIN roles ON roles_id = roles.id JOIN categories ON categories_id = categories.id WHERE champions.id = %(champion_id)s;'
#     data = {
#         "champion_id" : champion_id
#     }
#     champion = mysql.query_db(query,data)
#     return render_template("submittedForm.html", champion = champion[0])

# @app.route("/login")
# def login():
#     return render_template("login.html")










# @app.route("/authors/add", methods = ["POST"])
# def add_to_authors():
#     mysql = connectToMySQL('leaguechampionlog')
#     query = 'INSERT INTO authors(name,created_at,updated_at) VALUES(%(name)s,NOW(), NOW());'
#     data = {
#         "name": request.form["name"],
#     }
#     new_book = mysql.query_db(query,data)
#     # THIS IS A TEST
#     print(new_book)
#     return redirect("/")

# @app.route("/authors/show/<id>")
# def show_authors(id):
#     # Creating mysql object.
#     mysql = connectToMySQL('books_schema')
#     # creating a query and data for displaying current authors favorites.
#     query = 'SELECT books.title, books.num_of_pages FROM books JOIN favorites ON books.id = favorites.book_id WHERE favorites.author_id = %(id)s;'
#     data = {
#         "id" : id
#     }
#     # fetching query
#     favJoin = mysql.query_db(query,data)
#     # creating a query for all books
#     mysql = connectToMySQL('books_schema')
#     query = 'SELECT * FROM books;'
#     # fetching query
#     books = mysql.query_db(query,data)
#     return render_template("authors_show.html",favJoin = favJoin, books = books, id = id)

# @app.route("/authors/add/favorite/<author_id>", methods = ["POST"])
# def add_favorites_to_authors(author_id):
#     mysql = connectToMySQL('books_schema')
#     query = 'INSERT INTO favorites(book_id, author_id) VALUES(1,%(author_id)s);'
#     data = {
#         "author_id" : author_id,
#         "book_id": request.form["book"]
#     }
#     fav = mysql.query_db(query,data)
#     return redirect(f"/authors/show/{author_id}")

# @app.route("/books")
# def books():
#     mysql = connectToMySQL('books_schema')
#     # grabbing our authors and storing them in authors var as a string of dict.
#     books = mysql.query_db('SELECT * FROM books;')  # call the query_db function, pass in the query as a string
#     return render_template("books.html", books = books)

# @app.route("/books/add", methods = ["POST"])
# def add_to_books():
#     mysql = connectToMySQL('books_schema')
#     query = 'INSERT INTO books(title,num_of_pages,created_at,updated_at) VALUES(%(t)s, %(nP)s, NOW(), NOW());'
#     data = {
#         "t": request.form["title"],
#         "nP": request.form["numPages"]
#     }
#     new_book = mysql.query_db(query,data)
#     # THIS IS A TEST
#     print(new_book)
#     return redirect("/books")

# @app.route("/delete_friend/<user_num>")
# def delete(user_num):
#     mysql = connectToMySQL('users_schema')
#     query = 'DELETE FROM users WHERE id = %(user_num)s;'
#     data = {
#         "user_num": user_num
#     }
#     users = mysql.query_db(query,data)
#     print(users)
#     return redirect("/")

# @app.route("/show_person/<int:id>")
# def person(id):
#     mysql = connectToMySQL('users_schema')
#     query = 'SELECT * FROM users WHERE id = %(id)s;'
#     data = {
#         "id": id
#     }
#     users = mysql.query_db(query,data)
#     return render_template("individual.html", user = users[0])

# @app.route("/edit/<int:id>")
# def edit(id):
#     mysql = connectToMySQL('users_schema')
#     query = 'SELECT * FROM users WHERE id = %(id)s;'
#     data = {
#         "id": id
#     }
#     users = mysql.query_db(query,data)
#     return render_template("edit.html", user = users[0])

# @app.route("/edit_person/<int:id>", methods = ["POST"])
# def edit_person(id):
#     mysql = connectToMySQL('users_schema')
#     query = 'UPDATE users SET first_name = %(fn)s,last_name = %(ln)s,email = %(em)s WHERE id = %(id)s;'
#     data = {
#         "fn": request.form["fname"],
#         "ln": request.form["lname"],
#         "em": request.form["email"],
#         "id": id
#     }
#     mysql.query_db(query,data)
#     return redirect("/")

# @app.route("/create_friend", methods = ["POST"])
# def add_friend_to_db():
#     mysql = connectToMySQL('users_schema')
#     query = 'INSERT INTO users(first_name,last_name,email,created_at,updated_at) VALUES(%(fn)s, %(ln)s, %(em)s, NOW(), NOW());'
#     data = {
#         "fn": request.form["fname"],
#         "ln": request.form["lname"],
#         "em": request.form["email"]
#     }
#     new_user_id = mysql.query_db(query,data)
#     print(new_user_id)
#     return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)