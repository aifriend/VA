help:
	@echo "    eval"
	@echo "        Evaluate your trained model on a set of test stories by using the evaluate script"
	@echo "        This will print the failed stories to results/failed_stories.md."
	@echo "        We count any story as failed if at least one of the actions was predicted incorrectly."
	@echo "    compare CONFIG='example_config1.yml example_config2.yml...'"
	@echo "        To choose a specific policy, or to choose hyperparameters for a specific policy, you want to measure"
	@echo "        how well Rasa Core will generalise to conversations which it hasn’t seen before"
	@echo "    compare-eval"
	@echo "        Evaluate script in compare mode to evaluate the models you just trained"

eval:
	python -m rasa_core.evaluate --core models/dialogue --stories test/ -o results/ --endpoints endpoints.yml --debug

compare:
	python -m rasa_core.train compare -c $(CONFIG) -d data/domain.yml -s test/ -o comparison/models/ --runs 3 --percentages 0 5 25 50 70 90 95

compare-eval:
	python -m rasa_core.evaluate compare --stories test/ --core comparison/models/ -o comparison/results/ --endpoints endpoints.yml --debug
