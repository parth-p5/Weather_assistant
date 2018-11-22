.PHONY: clean train-nlu train-core cmdline server

TEST_PATH=./

help:
	@echo "    clean"
	@echo "        Remove python artifacts and build artifacts."
	@echo "    train-nlu"
	@echo "        Trains a new nlu model using the projects Rasa NLU config"
	@echo "    train-core"
	@echo "        Trains a new dialogue model using the story training data"

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf docs/_build

run-action:
	python -m rasa_core_sdk.endpoint --actions actions

train-nlu:
	python -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o models --fixed_model_name version1 --project nlu --verbose

train-core:
	python -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue --epochs 100

cmdline:
	python -m rasa_core.run -d models/dialogue -u models/nlu/version1 --enable_api --cors "*" --endpoints endpoints.yml
