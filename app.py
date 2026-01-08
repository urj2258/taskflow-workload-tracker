import os
from flask import Flask, render_template, request, redirect, url_for
from extensions import db
import models

app = Flask(__name__)

# Database Configuration
database_url = os.environ.get("DATABASE_URL")
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url or "sqlite:///taskflow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Ensure tables exist
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    tasks = models.get_all_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        priority = request.form["priority"]
        due_date = request.form["due_date"]

        models.create_task(title, description, priority, due_date)
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = models.get_task_by_id(task_id)

    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        priority = request.form["priority"]
        due_date = request.form["due_date"]
        status = request.form["status"]

        models.update_task(task_id, title, description, priority, due_date, status)
        return redirect(url_for("index"))

    return render_template("edit.html", task=task)


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    models.delete_task(task_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
