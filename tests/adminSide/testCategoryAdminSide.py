import json
import unittest
import requests
from tests.testHelper import Header, UrlCategory, CategoryPayloads
from dbconnection import Connection


class testCategoryAdminSide(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.header = Header().get_header_auth_admin()
        cls.conn = Connection()
        cls.conn.create_category_with_name("category to be deleted")

    def test_category_get_all(self):
        response_decoded_json = requests.get(UrlCategory.url_category_all, headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_category_edit_sea(self):
        response_decoded_json = requests.post(UrlCategory.url_category_edit,
                                              data=json.dumps(CategoryPayloads.category_to_edit), headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_create_category(self):
        response_decoded_json = requests.post(UrlCategory.url_category_edit,
                                              data=json.dumps(CategoryPayloads.category_to_create), headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)

    def test_delete_category(self):
        id = self.conn.get_id_using_name("category to be deleted")
        response_decoded_json = requests.get(UrlCategory.url_category_delete + self.conn.get_id_using_name("category to be deleted"),
                                             headers=self.header)
        self.assertEqual(200, response_decoded_json.status_code)


    @classmethod
    def tearDownClass(cls):
        cls.conn = Connection()
        cls.conn.delete_category_with_name("new")
        cls.conn.edit_category_with_name("MountNew", "Mount")
        cls.conn.close()


if __name__ == '__main__':
    unittest.main()
