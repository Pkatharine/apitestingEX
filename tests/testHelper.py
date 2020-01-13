import json

import requests


class UrlAuth:
    url_login = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/Login"
    url_register = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/Register"
    url_login_fb = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/FacebookLogin"
    url_login_google = "https://eventsexpress20200103054152.azurewebsites.net/api/Authentication/google"


class UrlCategory:
    url_category_edit = "https://eventsexpress20200103054152.azurewebsites.net/api/Category/Edit"
    url_category_all = "https://eventsexpress20200103054152.azurewebsites.net/api/Category/All"
    url_category_delete = "https://eventsexpress20200103054152.azurewebsites.net/api/Category/Delete/"


class AuthPayloads:
    payload_admin = {"Email": "admin@gmail.com", "Password": "1qaz1qaz"}
    payload_user = {"Email": "user@gmail.com", "Password": "1qaz1qaz"}
    payload_unauth = {"Email": "katya@gmail.com", "Password": "123"}

class CategoryPayloads:
    category_to_edit = {"Id": "F535A1D6-EEC4-4697-B4AD-08D7858FCA63", "Name": "MountNew"}
    category_to_create = {"Name": "new"}

class Header:
    header = {"accept": "application/json", "Content-Type": "application/json-patch+json"}

    def get_header_auth_admin(self):
        response_decoded_json = requests.post(UrlAuth.url_login, data=json.dumps(AuthPayloads.payload_admin),
                                              headers=Header.header)
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json",
                  "authorization": "Bearer " + auth}
        return header

    def get_header_auth_user(self):
        response_decoded_json = requests.post(UrlAuth.url_login, data=json.dumps(AuthPayloads.payload_user),
                                              headers=Header.header)
        h = json.loads(response_decoded_json.content.decode())
        auth = h["token"]
        header = {"accept": "application/json", "Content-Type": "application/json-patch+json",
                  "authorization": "Bearer " + auth}
        return header
