import json
import unittest
import requests
from dbconnection import Connection

class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url_login_FB = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/FacebookLogin"
        cls.url_login_Google = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/google"
        cls.header = {"accept": "application/json", "Content-Type": "application/json-patch+json"}

    def test_login_with_facebook(self):
        payload = {"Email": "user@gmail.com"}
        response_decoded_json = requests.post(self.url_login_FB, data=json.dumps(payload), headers=self.header)
        print(response_decoded_json.status_code)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_login_with_google(self):
        payload = {"Email": "admin@gmail.com"}
        response_decoded_json = requests.post(self.url_login_Google, data=json.dumps(payload), headers=self.header)
        print(response_decoded_json.status_code)
        self.assertEqual(400, response_decoded_json.status_code)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()