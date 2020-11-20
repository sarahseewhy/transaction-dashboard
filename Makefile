install:
	@pipenv install --dev

test:
	python3 -m pytest

run:
	@FLASK_APP=app/routes.py pipenv run flask run
