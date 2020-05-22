install:
	pipenv install

run:
	pipenv run python graph_experiments

build-docker:
	@docker build --no-cache -t bobas/learn_docker:local .
