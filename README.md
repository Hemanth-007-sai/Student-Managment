# Student Information Management System

Flask and SQLite project for Week 8(a) and Week 8(b). It has separate registration, login, and student-management modules, plus a JSON name-search endpoint.

## Run the application

In VS Code, open this folder and run these commands in its terminal:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

If this is a new setup without `.venv`, create it first with `python -m venv .venv`. Open `http://127.0.0.1:5000/`. The SQLite database and students table are initialized automatically. Passwords are stored as hashes. Do not use the classroom secret key or development server for a real deployment.

## Demonstrate Week 8(a)

1. Register with a name, email, password (at least six characters), and department.
2. Log in with that email and password.
3. View the student list and a student's details.
4. Edit a record and save it.
5. Delete a record and confirm it disappears.
6. Try an invalid login or submit missing registration fields to show validation.
7. In the terminal, run `git log --oneline --graph --all` to show the feature commits. The registration, login, and management branches were each created, committed, merged into `main`, and deleted. No merge conflicts occurred.

The Week 8(a) local repository should show only `main` after branch deletion. The database and virtual environments are excluded from Git.

## Demonstrate Week 8(b) search

With the Flask server running, open a URL such as:

```text
http://127.0.0.1:5000/search?name=alex&department=CSSE
```

The endpoint returns matching student IDs, names, emails, and departments as JSON. It searches partial names and can optionally filter by department. It uses parameterized SQLite values and does not return password hashes.

## GitHub workflow

The project is published in the `Student-Managment` repository. Clone it into a separate folder with:

```powershell
git clone https://github.com/Hemanth-007-sai/Student-Managment.git
cd Student-Managment
git remote -v
```

After cloning, the search endpoint can be extended and committed from that clone:

```powershell
git add app.py README.md
git commit -m "Enhance student search by department"
git push origin main
```

The project can also be pulled later with `git pull origin main`.
