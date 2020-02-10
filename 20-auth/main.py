from flask import Flask, render_template, redirect, url_for, request
from models import db, User

db.create_all()
app = Flask(__name__)

post_list = ["Eine Reise nach Indien", "Walfischen in Alaska", "Mal was ganz anderes"]

# GET ROUTES

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    # get posts from database
    return render_template("posts.html", posts=post_list)

@app.route("/enter-post")
def enter_post():
    return render_template("add-posts.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        #print("Hey, ich möchte nur das formular")
        return render_template("login.html")
    else:
        print("Hey ich möchte mich einloggen")
        # hole user anhand email aus der datenbank

        # vergleiche passwort aus datenbank mit eingebenem passwort

        # if korrekt
        return redirect("/posts")

        # else
        # redirect login

# POST ROUTES

@app.route("/add-post", methods=["POST"])
def add_post():
    new_post = request.form.get("title")
    # add post to database
    post_list.append(new_post)
    return redirect("/posts")


if __name__ == '__main__':
    app.run()