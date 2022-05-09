from unicodedata import name
import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.book import Book
from app.models.author import Author

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_books(app):
    # Arrange
    ocean_book = Book(title="Ocean Book",
                      description="watr 4evr")
    mountain_book = Book(title="Mountain Book",
                         description="i luv 2 climb rocks")

    db.session.add_all([ocean_book, mountain_book])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()

@pytest.fixture
def two_saved_authors(app):
    # Arrange
    author_SSL = Author(author_name="Shayla Logan")
    author_MRS = Author(author_name="Miss Sloth")

    db.session.add_all([author_SSL, author_MRS])
    # Alternatively, we could do
    # db.session.add(author_SSL)
    # db.session.add(author_MRS)
    db.session.commit()