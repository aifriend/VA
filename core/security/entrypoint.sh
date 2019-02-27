#!/bin/bash
gunicorn -b 0.0.0.0:8065 --access-logfile logs/gunicorn-access.log --error-logfile logs/gunicorn-error.log --log-level=DEBUG security_service:app