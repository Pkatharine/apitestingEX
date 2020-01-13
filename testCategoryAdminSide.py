import json
import unittest
import requests

from dbconnection import Connection


class testCategoryAdminSide(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url_category_all = "https://eventsexpress20200103054152.azurewebsites.net/api/Category/All"
        cls.url_category_edit = "https://eventsexpress20200103054152.azurewebsites.net/api/Category/Edit"
        cls.url_category_delete = "https://eventsexpress20200103054152.azurewebsites.net/api/Category/Delete/"
        cls.payload = {"Email": "admin@gmail.com", "Password": "1qaz1qaz"}
        cls.header = {"accept": "application/json", "Content-Type": "application/json-patch+json"}
        response_decoded_json = requests.post(
            "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/Login",
            data=json.dumps(cls.payload), headers=cls.header)
        h = json.loads(response_decoded_json.content.decode())
        cls.auth = h["token"]
        cls.header = {"accept": "application/json", "Content-Type": "application/json-patch+json",
                      "authorization": "Bearer " + cls.auth}

    def test_category_get_all(self):
        response_decoded_json = requests.get(self.url_category_all, headers=self.header)
        print(response_decoded_json.status_code)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_category_edit_sea(self):
        payload = {"Id": "F535A1D6-EEC4-4697-B4AD-08D7858FCA63", "Name": "MountNew"}
        response_decoded_json = requests.post(self.url_category_edit, data=json.dumps(payload), headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_create_category(self):
        payload = {"Name": "new"}
        response_decoded_json = requests.post(self.url_category_edit, data=json.dumps(payload), headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    @classmethod
    def tearDownClass(cls):
        cls.conn = Connection()
        cls.conn.delete_category_with_name("new")
        cls.conn.edit_category_with_name("MountNew", "Mount")
        cls.conn.close()


if __name__ == '__main__':
    unittest.main()
