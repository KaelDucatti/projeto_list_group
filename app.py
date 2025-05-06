from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    url_for, 
    session
)
from dotenv import load_dotenv
from os import environ


load_dotenv()

app = Flask(__name__)
app.secret_key = environ.get("FLASK_SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/users", methods=["GET", "POST"])
def users():
    if "users" not in session:
        session["users"] = []
    
    if request.method == "POST":
        user = {
            "name": request.form.get("name"),
            "age": request.form.get("age"),
            "gender": request.form.get("gender"),
            "email": request.form.get("email")
        }
        session["users"].append(user)
        session.modified = True

        return redirect(url_for("users"))
    return render_template("users.html", users=session["users"])


@app.route("/to_do_list", methods=["GET", "POST"])
def to_do_list():
    if "tasks" not in session:
        session["tasks"] = []

    if request.method == "POST":
        task = request.form.get("task")
        if task:
            session["tasks"].append(task)
            session.modified = True

        return redirect(url_for("to_do_list"))
    return render_template("to_do_list.html", tasks=session["tasks"])
