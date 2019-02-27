#!/bin/bash
#gunicorn -b 0.0.0.0:5005 --access-logfile logs/gunicorn-access.log --error-logfile logs/gunicorn-error.log usecase.callcenter.run:run_callcenter
python ./usecase/callcenter/run.py