#!/bin/bash
gunicorn -b 0.0.0.0:9000 --access-logfile logs/gunicorn-access.log --error-logfile logs/gunicorn-error.log --log-level=DEBUG config_service:app