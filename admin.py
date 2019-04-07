from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, url_prefix="/admin")


@admin.route("/")
def index():
    return render_template("admin/index.html")


@admin.route("/users")
def users():
    admin = "@bergpb"
    users = ["Usuario 1", "Usuario 2", "Usuario 3"]
    return render_template("admin/users.html", admin=admin, users=users)
