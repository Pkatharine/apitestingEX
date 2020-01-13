import json
import unittest
import requests
import allure
from tests.testHelper import UrlAuth, Header, AuthPayloads


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @allure.suite('Tests for "Contact us page"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("https://eventsexpress20200103054152.azurewebsites.net/home/events?page=1", name='Click me')
    @allure.story('Test loging with Facebook as user')
    def test_login_as_user_with_facebook(self):
        response_decoded_json = requests.post(UrlAuth.url_login_fb, data=json.dumps(AuthPayloads.payload_user),
                                              headers=Header.header)
        resp = response_decoded_json.json()
        with allure.step("Verification user's name"):
            self.assertEqual("UserTest", resp["name"], "You don't login with correct name")
        with allure.step("Verification user's role"):
            self.assertEqual("User", resp["role"], "You don't login with correct role")
        with allure.step("Verification status code"):
            self.assertEqual(200, response_decoded_json.status_code, "You have BAD REQUEST")

    @allure.link("https://eventsexpress20200103054152.azurewebsites.net/home/events?page=1", name='Click me')
    @allure.story('Test loging with Facebook as admin')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_as_admin_with_facebook(self):
        response_decoded_json = requests.post(UrlAuth.url_login_fb, data=json.dumps(AuthPayloads.payload_admin),
                                              headers=Header.header)
        resp = response_decoded_json.json()
        with allure.step("Verification admin's name"):
            self.assertEqual("Admin", resp["name"], "You don't login with correct name")
        with allure.step("Verification admin's role"):
            self.assertEqual("Admin", resp["role"], "You don't login with correct role")
        with allure.step("Verification status code"):
            self.assertEqual(200, response_decoded_json.status_code, "You have BAD REQUEST")

    @allure.link("https://eventsexpress20200103054152.azurewebsites.net/home/events?page=1", name='Click me')
    @allure.story('Test loging with Google as admin')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_google(self):
        response_decoded_json = requests.post(UrlAuth.url_login_google, data=json.dumps(AuthPayloads.payload_admin),
                                              headers=Header.header)
        with allure.step("Verification status code"):
            self.assertEqual(400, response_decoded_json.status_code, "You have BAD REQUEST")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == 'main':
    unittest.main()
