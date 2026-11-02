import sqlite3

from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from database import get_db
from login import login_required


management_bp = Blueprint("management", __name__)


def find_student(student_id):
    with get_db() as connection:
        student = connection.execute(
            "SELECT id, name, email, department FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()
    if student is None:
        abort(404)
    return student


@management_bp.route("/students")
@login_required
def students():
    with get_db() as connection:
        records = connection.execute(
            "SELECT id, name, email, department FROM students ORDER BY id DESC"
        ).fetchall()
    return render_template("students.html", students=records)


@management_bp.route("/students/<int:student_id>")
@login_required
def student_details(student_id):
    return render_template("student_detail.html", student=find_student(student_id))


@management_bp.route("/students/<int:student_id>/edit", methods=["GET", "POST"])
@login_required
def edit_student(student_id):
    student = find_student(student_id)
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        department = request.form.get("department", "").strip()
        if not all([name, email, department]):
            return render_template(
                "student_form.html",
                student=student,
                error="Name, email, and department are required.",
            ), 400
        if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
            return render_template(
                "student_form.html", student=student, error="Enter a valid email address."
            ), 400

        try:
            with get_db() as connection:
                connection.execute(
                    "UPDATE students SET name = ?, email = ?, department = ? WHERE id = ?",
                    (name, email, department, student_id),
                )
        except sqlite3.IntegrityError:
            return render_template(
                "student_form.html", student=student, error="That email is already in use."
            ), 409

        flash("Student record updated.", "success")
        return redirect(url_for("management.students"))

    return render_template("student_form.html", student=student)


@management_bp.route("/students/<int:student_id>/delete", methods=["POST"])
@login_required
def delete_student(student_id):
    find_student(student_id)
    with get_db() as connection:
        connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
    deleting_current_user = student_id == session.get("student_id")
    if deleting_current_user:
        session.clear()
    flash("Student record deleted.", "success")
    return redirect(
        url_for("home" if deleting_current_user else "management.students")
    )
