import json
import unittest
import requests
from tests_api.config import URL_AUTH, HEADER, AUTH_PAYLOADS


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_login_as_user_with_facebook(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login_fb'], data=json.dumps(
                AUTH_PAYLOADS['payload_user']), headers=HEADER['header'])
        resp = response_decoded_json.json()
        self.assertEqual(
            "UserTest",
            resp["name"],
            "You don't login with correct name")
        self.assertEqual(
            "User",
            resp["role"],
            "You don't login with correct role")
        self.assertEqual(
            200,
            response_decoded_json.status_code,
            "You have BAD REQUEST")

    def test_login_as_admin_with_facebook(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login_fb'], data=json.dumps(
                AUTH_PAYLOADS['payload_admin']), headers=HEADER['header'])
        resp = response_decoded_json.json()
        self.assertEqual(
            "Admin",
            resp["name"],
            "You don't login with correct name")
        self.assertEqual(
            "Admin",
            resp["role"],
            "You don't login with correct role")
        self.assertEqual(
            200,
            response_decoded_json.status_code,
            "You have BAD REQUEST")

    def test_login_with_google(self):
        response_decoded_json = requests.post(
            URL_AUTH['url_login_google'], data=json.dumps(
                AUTH_PAYLOADS['payload_admin']), headers=HEADER['header'])
        self.assertEqual(400, response_decoded_json.status_code)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
