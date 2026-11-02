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
http://127.0.0.1:5000/search?name=alex
```

The endpoint returns matching student IDs, names, emails, and departments as JSON. It uses a parameterized SQLite query and does not return password hashes.

## Connect to GitHub

Create an empty GitHub repository named `StudentManagement` (do not initialize it with a README). Then, from this project folder, replace `USERNAME` with your GitHub username and run:

```powershell
git remote add origin https://github.com/USERNAME/StudentManagement.git
git push -u origin main
```

To clone it into another folder and inspect the history:

```powershell
cd ..
git clone https://github.com/USERNAME/StudentManagement.git
cd StudentManagement
git remote -v
```

The project files are ready for this remote workflow. The GitHub repository has not been created or pushed because its owner account and repository URL have not been provided.
