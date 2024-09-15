from app.infra.api.app import create_app
from app.config.test import TestConfig
import unittest
import json

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Clean up after tests"""
        self.app_context.pop()

    def test_root_endpoint(self):
        """Test root endpoint"""
        response = self.client.get('/')
        obj = json.loads(str(response.data.decode('utf-8')))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(obj['success'], True)

if __name__ == '__main__':
    unittest.main()