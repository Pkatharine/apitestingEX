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
        self.assertEqual(200, response_decoded_json.status_code)

    def test_login_user(self):
        response_decoded_json = requests.post(UrlAuth.url_login, data=json.dumps(AuthPayloads.payload_user),
                                              headers=Header.header)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_unauthorized_user(self):
        response_decoded_json = requests.post(UrlAuth.url_login, data=json.dumps(AuthPayloads.payload_unauth),
                                              headers=Header.header)
        self.assertEqual(400, response_decoded_json.status_code)

    def test_register_already_exist(self):
        response_decoded_json = requests.post(UrlAuth.url_register, data=json.dumps(AuthPayloads.payload_user),
                                              headers=Header.header)
        self.assertEqual(400, response_decoded_json.status_code)

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
