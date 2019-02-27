#!/bin/bash
gunicorn -b 0.0.0.0:8075 --access-logfile logs/gunicorn-access.log --error-logfile logs/gunicorn-error.log --log-level=DEBUG watson_service:app