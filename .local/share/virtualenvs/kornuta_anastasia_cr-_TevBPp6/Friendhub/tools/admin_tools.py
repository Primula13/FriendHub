import requests
from Friendhub.configurations import models

uri1 = "http://friendhub.dev.cleveroad.com/api/v1/"
uri2 = "http://friendhub.dev.cleveroad.com/admin/api/v1/"


def admin_auth(email, password):
    payload = {"email": email, "password": password}
    r = requests.post(url=uri1 + 'signin/admin', data=payload)
    result = list()
    result.append(r.status_code)
    result.append(r.json())
    return result


def change_pass_admin(new_pass, old_pass):
    auth_header = {"Authorization": models.admin.token}
    payload = {"password": new_pass, "oldPassword": old_pass}
    r = requests.patch(url=uri2 + 'profile/password', headers=auth_header, data=payload)
    result = list()
    result.append(r.status_code)
    if r.status_code != 200:
        result.append(r.json()['validation'][0]['message'])
    return result


def change_name(first_name, last_name):
    auth_header = {"Authorization": models.admin.token}
    payload = {"firstName": first_name, "lastName": last_name}
    r = requests.put(url=uri1 + 'profile', headers=auth_header, data=payload)
    result = list()
    result.append(r.status_code)
    result.append(r.json())
    return result
