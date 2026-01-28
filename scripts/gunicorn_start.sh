#!/bin/bash

echo "Starting Gunicorn..."
exec gunicorn app.main:app --config gunicorn.conf.py

