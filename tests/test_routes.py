import unittest
import pytest
from flask import url_for
from context import app


class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()


    def test_zones_url(self):
        rv = self.app.get('/zones')

        assert rv.status_code != 404
