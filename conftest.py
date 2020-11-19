import pytest

from app.routes import app
from config import load_environment


@pytest.fixture()
def test_client():
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = app.test_client()
    load_environment(app)

    # Establish an application context before running the tests.
    context = app.app_context()
    context.push()

    yield testing_client  # this is where the testing happens!

    context.pop()
