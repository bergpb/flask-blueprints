from flask import Flask, jsonify, render_template
from admin import admin

app = Flask(__name__)
app.register_blueprint(admin)


@app.route("/")
def index():
    return jsonify({"message": "Hello Flask!"})


@app.route("/hello")
def hello():
    return render_template("index.html")


@app.route("/posts")
def posts():
    nome = "Berg"
    posts = ["Flask Basico", "Flask Intermediario", "Flask Avancado"]
    return render_template("posts.html", nome=nome, posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
