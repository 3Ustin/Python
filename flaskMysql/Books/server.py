from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
# import the function that will return an instance of a connection
app = Flask(__name__)


@app.route("/")
def index():
    mysql = connectToMySQL('books_schema')
    # grabbing our authors and storing them in authors var as a string of dict.
    authors = mysql.query_db('SELECT * FROM authors;')  # call the query_db function, pass in the query as a string
    return render_template("authors.html", authors = authors)

@app.route("/authors/add", methods = ["POST"])
def add_to_authors():
    mysql = connectToMySQL('books_schema')
    query = 'INSERT INTO authors(name,created_at,updated_at) VALUES(%(name)s,NOW(), NOW());'
    data = {
        "name": request.form["name"],
    }
    new_book = mysql.query_db(query,data)
    # THIS IS A TEST
    print(new_book)
    return redirect("/")

@app.route("/authors/show/<id>")
def show_authors(id):
    # Creating mysql object.
    mysql = connectToMySQL('books_schema')
    # creating a query and data for displaying current authors favorites.
    query = 'SELECT books.title, books.num_of_pages FROM books JOIN favorites ON books.id = favorites.book_id WHERE favorites.author_id = %(id)s;'
    data = {
        "id" : id
    }
    # fetching query
    favJoin = mysql.query_db(query,data)
    # creating a query for all books
    mysql = connectToMySQL('books_schema')
    query = 'SELECT * FROM books;'
    # fetching query
    books = mysql.query_db(query,data)
    return render_template("authors_show.html",favJoin = favJoin, books = books, id = id)

@app.route("/authors/add/favorite/<author_id>", methods = ["POST"])
def add_favorites_to_authors(author_id):
    mysql = connectToMySQL('books_schema')
    query = 'INSERT INTO favorites(book_id, author_id) VALUES(1,%(author_id)s);'
    data = {
        "author_id" : author_id,
        "book_id": request.form["book"]
    }
    fav = mysql.query_db(query,data)
    return redirect(f"/authors/show/{author_id}")

@app.route("/books")
def books():
    mysql = connectToMySQL('books_schema')
    # grabbing our authors and storing them in authors var as a string of dict.
    books = mysql.query_db('SELECT * FROM books;')  # call the query_db function, pass in the query as a string
    return render_template("books.html", books = books)

@app.route("/books/add", methods = ["POST"])
def add_to_books():
    mysql = connectToMySQL('books_schema')
    query = 'INSERT INTO books(title,num_of_pages,created_at,updated_at) VALUES(%(t)s, %(nP)s, NOW(), NOW());'
    data = {
        "t": request.form["title"],
        "nP": request.form["numPages"]
    }
    new_book = mysql.query_db(query,data)
    # THIS IS A TEST
    print(new_book)
    return redirect("/books")

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