install:
	@pipenv install

test:
	pipenv run pytest

run:
	@FLASK_APP=app/routes.py pipenv run flask run
