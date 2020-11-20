install:
	@pipenv install

test:
	python3 -m pytest

run:
	@FLASK_APP=app/routes.py pipenv run flask run
