from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "4948d2d8b93d58cb96200fb3d8ba4593"

posts = [
    {
        "author": "Utkarsh Chauhan",
        "title": "Blop Post 1",
        "content": "First post content",
        "date_posted": "April 5, 2021",
    },
    {
        "author": "Jane Doe",
        "title": "Blop Post 2",
        "content": "Second post content",
        "date_posted": "April 20, 2021",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("Logged In Successfully", "success")
            return redirect(url_for("home"))
        else:
            flash("Incorrect username or password. Please try again", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
