import os

CONFIG = {}


def load_environment(app):
    """
    Load environment vars into flask app attributes
    """
    global CONFIG
    CONFIG = app.config
    setup_local_environment()


def setup_local_environment():
    CONFIG['CLIENT_ID'] = os.getenv('CLIENT_ID')
    CONFIG['REDIRECT_URL'] = os.getenv('REDIRECT_URL')
    CONFIG['ENV'] = "development"
    CONFIG['TESTING'] = True
    CONFIG['SERVER_NAME'] = 'localhost:5000'
