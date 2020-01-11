import json
import unittest
import requests
from dbconnection import Connection

class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url_login = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/Login"
        cls.url_register = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/Register"
        cls.header = {"accept": "application/json", "Content-Type": "application/json-patch+json"}

    def test_login_admin(self):
        payload = {"Email": "admin@gmail.com", "Password": "1qaz1qaz"}
        response_decoded_json = requests.post(self.url_login, data=json.dumps(payload), headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_login_user(self):
        payload = {"Email": "user@gmail.com", "Password": "1qaz1qaz"}
        response_decoded_json = requests.post(self.url_login, data=json.dumps(payload), headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_unauthorized_user(self):
        payload = {"Email": "katya@gmail.com", "Password": "123"}
        response_decoded_json = requests.post(self.url_login, data=json.dumps(payload), headers=self.header)
        self.assertEqual(400, response_decoded_json.status_code)

    def test_register_already_exist(self):
        payload = {"Email": "user@gmail.com", "Password": "1qaz1qaz"}
        response_decoded_json = requests.post(self.url_register, data=json.dumps(payload), headers=self.header)
        self.assertEqual(400, response_decoded_json.status_code)

    def test_register_new_user(self):
        payload = {"Email": "katya@gmail.com", "Password": "1qaz1qaz"}
        response_decoded_json = requests.post(self.url_register, data=json.dumps(payload), headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    @classmethod
    def tearDownClass(cls):
        cls.conn = Connection()
        cls.conn.delete_user_with_email("katya@gmail.com")
        cls.conn.close()

if __name__ == '__main__':
    unittest.main()
