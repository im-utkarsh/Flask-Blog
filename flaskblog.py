from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
