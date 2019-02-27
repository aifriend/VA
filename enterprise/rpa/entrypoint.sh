#!/bin/bash
gunicorn -b 0.0.0.0:8095 --access-logfile logs/gunicorn-access.log --error-logfile logs/gunicorn-error.log --log-level=DEBUG rpa_service:app