import sqlite3

from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

from database import get_db


registration_bp = Blueprint("registration", __name__)


@registration_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        department = request.form.get("department", "").strip()

        if not all([name, email, password, department]):
            return render_template(
                "register.html", error="All fields are required."
            ), 400
        if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
            return render_template(
                "register.html", error="Enter a valid email address."
            ), 400
        if len(password) < 6:
            return render_template(
                "register.html", error="Password must be at least 6 characters."
            ), 400

        try:
            with get_db() as connection:
                connection.execute(
                    """INSERT INTO students (name, email, password, department)
                       VALUES (?, ?, ?, ?)""",
                    (name, email, generate_password_hash(password), department),
                )
        except sqlite3.IntegrityError:
            return render_template(
                "register.html", error="That email is already registered."
            ), 409

        return redirect(url_for("login.login"))

    return render_template("register.html")
