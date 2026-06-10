import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = Trueееее

    def test_index_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_json_status(self):
        response = self.client.get('/')
        data = response.get_json()
        self.assertEqual(data['status'], 'ok')

    def test_health_returns_200(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_health_json_status(self):
        response = self.client.get('/health')
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')

if __name__ == '__main__':
    unittest.main()
