# local-ci-cd-flask-app
# Production Flask App (Gunicorn + NGINX + CI/CD)

## Tech Stack
- Python (Flask)
- Gunicorn
- NGINX
- GitHub Actions
- WSL (Ubuntu)

## Architecture
Client → NGINX → Gunicorn → Flask

## How to Run Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn app.main:app
 
