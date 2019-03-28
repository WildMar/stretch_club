import pytest

from app import app


@pytest.fixture
def test_app():
    """ This fixture will provides a simple interface to the application,
    where we can trigger test requests to the application. """

    # Create temporary database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
    app.config["TESTING"] = True

    client = app.test_client()
    with app.app_context():
        app.init_db()
    yield client
