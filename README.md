# Snyk Code Lab – Student Course Registration Demo

This repository is intentionally vulnerable and is designed for a Software
Quality Assurance/Snyk Code laboratory exercise.

## Files
- `app.py` — intentionally vulnerable Flask application
- `requirements.txt` — dependency file
- `README.md` — setup/scanning notes

## Intended Snyk Code findings
The code contains examples of:
1. SQL injection
2. Command injection
3. Hard-coded credentials/secrets
4. Potential path traversal
5. Weak MD5 password hashing
6. Debug mode enabled

## GitHub + Snyk workflow
1. Create a new GitHub repository, e.g. `snyk-course-registration-lab`.
2. Upload `app.py`, `requirements.txt`, and `README.md`.
3. In Snyk, connect/import the GitHub repository.
4. Run a Snyk Code scan.
5. Record each finding, severity, affected file/line, explanation, and remediation.
6. Take screenshots for the Lab 4 evidence section.

IMPORTANT: This project is intentionally vulnerable for educational scanning only.
Do not deploy it publicly or reuse its credentials/secrets in a real application.
