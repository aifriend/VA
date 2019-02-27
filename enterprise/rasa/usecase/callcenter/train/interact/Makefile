DATA_PATH=data/

help:
	@echo "    train-interactive"
	@echo "        Build a dialogue flow in an interactive mode"
	@echo "    train-core-py"
	@echo "        Train a dialogue model using Rasa core from file.py."
	@echo "    train-interactive-py"
	@echo "        Train a dialogue model using Interactive Rasa core from file.py (Need run NLG and ACTIONS first!)."
	@echo "    visualize-core"
	@echo "        Show your stories as a graph"
	@echo "    visualize-interactive"
	@echo "        Show your interactive stories as a graph"
	@echo "    train-nlu"
	@echo "        Train a linguistic model using Rasa nlu."
	@echo "    train-interactive-nlu"
	@echo "        Build a dialogue flow in an interactive mode with nlu support"
	@echo "    show-process"
	@echo "        Show network PORT taken."

train-interactive:
	python -m rasa_core.train interactive -s $(DATA_PATH)story/ -d $(DATA_PATH)domain/domain.yml -o models/dialogue --endpoints endpoints.yml --augmentation 0 -c policy.yml --debug

train-interactive-py:
	python train_interact.py

visualize-interactive:
	python -m rasa_core.visualize -s $(DATA_PATH)story/ -d $(DATA_PATH)domain/domain.yml -o $(DATA_PATH)display/story_graph.html -c policy.yml

train-interactive-nlu:
	python -m rasa_core.train interactive -s $(DATA_PATH)story/ -d $(DATA_PATH)domain/domain.yml -o models/dialogue --nlu models/nlu/current --endpoints endpoints.yml -c policy.yml --debug

train-nlu:
	python -m rasa_nlu.train -c models/nlu/nlu_tensorflow.yml --fixed_model_name current --data nlu/nlu_data.md -o models --project nlu --verbose

show-process:
	netstat -vanp tcp | grep $(PORT)
