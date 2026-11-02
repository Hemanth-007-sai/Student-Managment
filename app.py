import os

from flask import Flask, jsonify, render_template, request

from database import get_db, init_db
from login import login_bp
from management import management_bp
from registration import registration_bp

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "classroom-demo-only-secret")
app.register_blueprint(registration_bp)
app.register_blueprint(login_bp)
app.register_blueprint(management_bp)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search_student():
    name = request.args.get("name", "").strip()
    department = request.args.get("department", "").strip()
    filters = ["name LIKE ? COLLATE NOCASE"]
    values = [f"%{name}%"]
    if department:
        filters.append("department LIKE ? COLLATE NOCASE")
        values.append(f"%{department}%")

    with get_db() as connection:
        records = connection.execute(
            f"""SELECT id, name, email, department FROM students
                WHERE {' AND '.join(filters)} ORDER BY name LIMIT 100""",
            values,
        ).fetchall()
    return jsonify([dict(record) for record in records])


init_db()


if __name__ == "__main__":
    app.run(debug=True)
