import requests

allureServer = 'http://192.168.99.100:5050' #localhost


def allure_get_status():
    response = requests.get(allureServer)
    if response.status_code == 200:
        return ('Request success!')
    elif response.status_code == 400:
        return ('Bad request!')



def allure_api_get(api):
    return requests.get(allureServer + '/'+ api)