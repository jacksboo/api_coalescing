import unittest

from api_handler import APIHAndler
from app import app_setup


class TestAPIHandler(unittest.TestCase):
    def test_avg_strategy(self):
        api_handler = APIHAndler(member_id=1, strategy='avg')
        data = api_handler.get_data()
        assert data == {'deductible': 1066, 'stop_loss': 11000, 'oop_max': 5666}

    def test_min_strategy(self):
        api_handler = APIHAndler(member_id=1, strategy='min')
        data = api_handler.get_data()
        assert data == {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 5000}

    def test_max_strategy(self):
        api_handler = APIHAndler(member_id=1, strategy='max')
        data = api_handler.get_data()

        assert data == {'deductible': 1200, 'stop_loss': 13000, 'oop_max': 6000}


class TestEndpoints(unittest.TestCase):
    app = app_setup()
    client = app.test_client()

    def test_client_without_member_400(self):
        response = self.client.get('/api/data')
        assert response.status_code == 400

    def test_client_with_member_200(self):
        response = self.client.get('/api/data?member_id=1')
        assert response.status_code == 200

    def test_client_welcome_homepage_200(self):
        response = self.client.get('/')
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()