.PHONY: clean-upload

Help:
	@echo "    clean-upload"
	@echo "        Clean project to be uploaded to production"
	@echo "    clean-logs"
	@echo "        Clean all proyect logs"
	@echo "    copy-config"
	@echo "        Copy config.py to its original places"
	@echo "    clean-model"
	@echo "        Clean project rasa model"
	@echo "    clean-mongo"
	@echo "        Clean mongo data base"
	@echo "    clean-model"
	@echo "        Clean rasa trained model"
	@echo "    show-process"
	@echo "        Show network PORT taken"

clean-build:
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-logs:
	find . -name '*.log' -exec rm -f {} +
	find . -name '*.log.*' -exec rm -f {} +

clean-data:
	rm -f enterprise/rasa/domain.md
	rm -f enterprise/rasa/data/*
	rm -f enterprise/rasa/story_graph.dot
	rm -f enterprise/rasa/usecase/callcenter/data/display/story_core_graph.html

clean-model:
	find enterprise/rasa/usecase/callcenter/models/ -name '*' -exec rm -fr {} +

clean-mongo:
	find deploy/docker/rasa_core/tracker_store/data/ -name '*' -exec rm -fr {} +

clean-config:
	rm -f core/configuration/config.py
	rm -f core/context/config.py
	rm -f core/confidence/config.py
	rm -f core/security/config.py
	rm -f core/business/config.py
	rm -f core/dialog/config.py
	rm -f enterprise/sap/config.py
	rm -f enterprise/rpa/config.py
	rm -f enterprise/watson/config.py
	rm -f enterprise/rasa/usecase/callcenter/config.py
	rm -f enterprise/rasa/usecase/callcenter/action/config.py
	rm -f enterprise/rasa/usecase/callcenter/nlg/config.py

copy-config:
	cp config.py core/configuration/config.py
	cp config.py core/context/config.py
	cp config.py core/confidence/config.py
	cp config.py core/security/config.py
	cp config.py core/business/config.py
	cp config.py core/dialog/config.py
	cp config.py enterprise/sap/config.py
	cp config.py enterprise/rpa/config.py
	cp config.py enterprise/watson/config.py
	cp config.py enterprise/rasa/usecase/callcenter/config.py
	cp config.py enterprise/rasa/usecase/callcenter/action/config.py
	cp config.py enterprise/rasa/usecase/callcenter/nlg/config.py

clean-upload:
	make clean-build
	make clean-pyc
	make clean-logs
	make clean-data
	make clean-model

show-process:
	netstat -vanp tcp | grep $(PORT)
