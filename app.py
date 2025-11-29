from flask import Flask, render_template, redirect, request
from models import db, Task

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()

    return redirect("/")

@app.route("/delete/<int:id>")
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

@app.route("/complete/<int:id>")
def complete_task(id):
    task = Task.query.get(id)
    task.complete = True
    db.session.commit()

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)