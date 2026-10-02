"""
Snyk Code Lab Demo - Student Course Registration System
INTENTIONALLY VULNERABLE: for SQA/Snyk scanning practice only.
Do not deploy this application publicly.
"""
import sqlite3
import subprocess
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = "courses.db"

# Hard-coded secret for scanner demonstration.
ADMIN_PASSWORD = "Admin@123"
SECRET_KEY = "my-super-secret-key-123"

def get_db():
    return sqlite3.connect(DATABASE)

@app.route("/login", methods=["POST"])
def login():
    student_id = request.form.get("student_id", "")
    password = request.form.get("password", "")

    # SQL injection: user input is concatenated into SQL.
    db = get_db()
    query = ("SELECT student_id FROM students WHERE student_id = '"
             + student_id + "' AND password = '" + password + "'")
    row = db.execute(query).fetchone()
    db.close()

    if row:
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/register", methods=["POST"])
def register():
    student_id = request.form.get("student_id", "")
    course_id = request.form.get("course_id", "")

    # SQL injection: registration data is concatenated into SQL.
    db = get_db()
    query = ("INSERT INTO registrations(student_id, course_id) VALUES ('"
             + student_id + "', '" + course_id + "')")
    try:
        db.execute(query)
        db.commit()
        return jsonify({"message": "Course registered"})
    finally:
        db.close()

@app.route("/search", methods=["GET"])
def search_courses():
    keyword = request.args.get("keyword", "")

    # SQL injection in course search.
    db = get_db()
    query = "SELECT * FROM courses WHERE name LIKE '%" + keyword + "%'"
    rows = db.execute(query).fetchall()
    db.close()
    return jsonify({"courses": rows})

@app.route("/run-report", methods=["POST"])
def run_report():
    report_name = request.form.get("report_name", "")

    # Command injection: untrusted input reaches a shell.
    command = "python generate_report.py " + report_name
    result = subprocess.check_output(command, shell=True, text=True)
    return jsonify({"report": result})

@app.route("/student-file", methods=["GET"])
def student_file():
    filename = request.args.get("filename", "")

    # Potential path traversal: filename is used directly.
    with open("student_files/" + filename, "r", encoding="utf-8") as f:
        return f.read()

@app.route("/hash-password", methods=["POST"])
def hash_password():
    password = request.form.get("password", "")

    # Weak cryptographic hash for password handling.
    password_hash = hashlib.md5(password.encode()).hexdigest()
    return jsonify({"hash": password_hash})

if __name__ == "__main__":
    # Debug mode is intentionally enabled for scanner demonstration.
    app.run(host="127.0.0.1", port=5000, debug=True)
