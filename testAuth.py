import json
import unittest
import requests
from dbconnection import Connection
from testHelper import UrlAuth, Header, AuthPayloads


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_login_admin(self):
        response_decoded_json = requests.post(UrlAuth.url_login, data=json.dumps(AuthPayloads.payload_admin),
                                              headers=Header.header)
        resp = response_decoded_json.json()
        print(resp["role"])
        self.assertEqual("Admin", resp["role"], "You don't login with correct role")
        self.assertEqual(200, response_decoded_json.status_code, "You have BAD REQUEST")
    def test_login_user(self):
        response_decoded_json = requests.post(UrlAuth.url_login, data=json.dumps(AuthPayloads.payload_user),
                                              headers=Header.header)
        resp = response_decoded_json.json()
        print(resp["role"])
        self.assertEqual("User", resp["role"], "You don't login with correct role")
        self.assertEqual(200, response_decoded_json.status_code, "You have BAD REQUEST")
    def test_unauthorized_user(self):
        response_decoded_json = requests.post(UrlAuth.url_login, data=json.dumps(AuthPayloads.payload_unauth),
                                              headers=Header.header)
        mes = response_decoded_json.json()
        self.assertEqual("User not found", mes, "This user is not registered")
        self.assertEqual(400, response_decoded_json.status_code, "You have BAD REQUEST")
    def test_register_already_exist(self):
        response_decoded_json = requests.post(UrlAuth.url_register, data=json.dumps(AuthPayloads.payload_user),
                                              headers=Header.header)
        mes = response_decoded_json.json()
        self.assertEqual("Email already exists in database", mes, "There is no such email in the database")
        self.assertEqual(400, response_decoded_json.status_code, "You have BAD REQUEST")

    def test_register_new_user(self):
        response_decoded_json = requests.post(UrlAuth.url_register, data=json.dumps(AuthPayloads.payload_unauth),
                                              headers=Header.header)
        self.assertEqual(200, response_decoded_json.status_code)

    @classmethod
    def tearDownClass(cls):
        cls.conn = Connection()
        cls.conn.delete_user_with_email("katya@gmail.com")
        cls.conn.close()

if __name__ == '__main__':
    unittest.main()
