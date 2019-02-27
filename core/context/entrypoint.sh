#!/bin/bash
gunicorn -b 0.0.0.0:8050 --access-logfile logs/gunicorn-access.log --error-logfile logs/gunicorn-error.log --log-level=DEBUG context_manager:app