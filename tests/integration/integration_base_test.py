"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    def setUp(self):

        # (the method runs before every test)
        # make sure database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()

        # get a test client
        self.app = app.test_client()
        self.app_context = app.app_context()

    def tearDown(self):
        # (the method runs after every test)
        # database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()

