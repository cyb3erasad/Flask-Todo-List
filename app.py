from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from flask_bcrypt import Bcrypt
from models import db, Task, User


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SECRET_KEY"] = "e2f9a6d4c583"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(username = username, password = hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect("/")
    return render_template("login.html")
          
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")



@app.route("/")
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
@login_required
def add_task():
    title = request.form.get("title")
    new_task = Task(title=title, user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()

    return redirect("/")

@app.route("/delete/<int:id>")
@login_required
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

@app.route("/complete/<int:id>")
@login_required
def complete_task(id):
    task = Task.query.get(id)
    task.complete = True
    db.session.commit()

    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_task(id):
    task = Task.query.get_or_404(id)

    if task.user_id != current_user.id:
        return "Unauthorized", 403
    
    if request.method == "POST":
        task.title = request.form["title"]
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", task=task)

if __name__ == "__main__":
    app.run(debug=True)