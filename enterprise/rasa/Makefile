.PHONY: clean test lint

PROJ_PATH=usecase/callcenter
DATA_PATH=$(PROJ_PATH)/data
TRAIN_PATH=$(PROJ_PATH)/train/interact

help:
	@echo "    run"
	@echo "        Spin up both core, the action server, the duckling server and the nlg server"
	@echo "    run-core-py"
	@echo "        Run core server for rasaio channel"
	@echo "    run-backend"
	@echo "        Run NLG and Action server for rasa-core from the command line"
	@echo "    run-core"
	@echo "        Spin up the core rest on the command line"
	@echo "    run-core-api"
	@echo "        Spin up the core api rest on the command line"
	@echo "    run-core-server"
	@echo "        Spin up the core server on the command line"
	@echo "    run-core-channel"
	@echo "        Spin up the core server with the api channel on the command line"
	@echo "    train-interactive"
	@echo "        Build a dialogue flow in an interactive mode"
	@echo "    visualize"
	@echo "        Show your stories as a graph"
	@echo "    clean"
	@echo "        Clean python stuff"
	@echo "    show-process"
	@echo "        Show network PORT taken."

run:
	make run-core

run-core-py:
	python $(PROJ_PATH)/run.py

run-core:
	python -m rasa_core.run -d $(PROJ_PATH)/models/dialogue -o $(PROJ_PATH)/logs/rasa_core.log --endpoints endpoints-dev.yml --debug

run-core-api:
	python -m rasa_core.run --enable_api -d $(PROJ_PATH)/models/dialogue -o $(PROJ_PATH)/logs/rasa_core.log --endpoints endpoints-dev.yml --debug

visualize:
	python -m rasa_core.visualize -s $(DATA_PATH)/story/ -d $(DATA_PATH)/domain/domain.yml -o $(DATA_PATH)/display/story_graph.html

train-interactive:
	python -m rasa_core.train interactive -s $(DATA_PATH)/story/ -d $(DATA_PATH)/domain/domain.yml -o $(PROJ_PATH)/models/dialogue --endpoints endpoints-dev.yml -c $(TRAIN_PATH)/policy.yml --debug

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean:
	make clean-build
	make clean-pyc

show-process:
	netstat -vanp tcp | grep $(PORT)