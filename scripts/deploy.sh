#!/bin/bash
set -e

echo "Activating virtual environment"
source venv/bin/activate

echo "Installing dependencies"
pip install -r requirements.txt

echo "Restarting Gunicorn service"
sudo systemctl restart flask_app

echo "Deployment completed successfully"

