import json
import unittest
import requests


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_login_as_user_with_facebook(self):
        url_login_fb = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/FacebookLogin"
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json"}
        payload = {"Email": "user@gmail.com"}
        response_decoded_json = requests.post(url_login_fb, data=json.dumps(payload), headers=header)
        resp = response_decoded_json.json()
        self.assertEqual("UserTest", resp["name"], "You don't login with correct name")
        self.assertEqual("User", resp["role"], "You don't login with correct role")
        self.assertEqual(200, response_decoded_json.status_code, "You have BAD REQUEST")

    def test_login_as_admin_with_facebook(self):
        url_login_fb = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/FacebookLogin"
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json"}
        payload = {"Email": "admin@gmail.com"}
        response_decoded_json = requests.post(url_login_fb, data=json.dumps(payload), headers=header)
        resp = response_decoded_json.json()
        self.assertEqual("Admin", resp["name"], "You don't login with correct name")
        self.assertEqual("Admin", resp["role"], "You don't login with correct role")
        self.assertEqual(200, response_decoded_json.status_code, "You have BAD REQUEST")

    def test_login_with_google(self):
        url_login_google = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/google"
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json"}
        payload = {"Email": "admin@gmail.com"}
        response_decoded_json = requests.post(url_login_google, data=json.dumps(payload), headers=header)
        self.assertEqual(400, response_decoded_json.status_code, "You have BAD REQUEST")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
