import unittest
from app import app

class TestCloudApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        # Sends an HTTP GET request to '/'
        response = self.app.get('/')
        # Check if the server responded with 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the content is correct
        self.assertEqual(response.data.decode('utf-8'), "Cloud App is Running!")

if __name__ == '__main__':
    unittest.main()