from functools import wraps

from flask import Blueprint, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash

from database import get_db


login_bp = Blueprint("login", __name__)


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "student_id" not in session:
            return redirect(url_for("login.login"))
        return view(*args, **kwargs)

    return wrapped_view


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        with get_db() as connection:
            student = connection.execute(
                "SELECT id, name, email, password FROM students WHERE email = ?",
                (email,),
            ).fetchone()

        if student is None or not student["password"] or not check_password_hash(
            student["password"], password
        ):
            return render_template(
                "login.html", error="Email or password is incorrect."
            ), 401

        session.clear()
        session["student_id"] = student["id"]
        session["student_name"] = student["name"]
        return redirect(url_for("management.students"))

    return render_template("login.html")


@login_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("home"))
