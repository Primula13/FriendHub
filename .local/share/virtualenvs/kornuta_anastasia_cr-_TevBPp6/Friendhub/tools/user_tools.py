import requests

from Friendhub.configurations import models

uri = "http://friendhub.dev.cleveroad.com/api/v1/"
token = models.user1.token


def get_user_profile_auth():
    auth_header = {"Authorization": token}
    r = requests.get(url=uri + 'users/9/detail', headers=auth_header)
    result = list()
    if r.status_code == 200:
        result.append(r.status_code)
        result.append(r.json())
    elif r.status_code != 200:
        result.append(r.status_code)
        result.append(r.json()['validation'][0]['message'])
    return result


def user_auth(email, password):
    payload = {"email": email, "password": password}
    r = requests.post(url=uri + 'signin/basic', data=payload)
    result = list()
    result.append(r.status_code)
    result.append(r.json())
    return result


def change_pass_user(new_password, old_password):
    auth_header = {"Authorization": token}
    payload = {"password": new_password, "oldPassword": old_password}
    r = requests.patch(url=uri + 'users/password', headers=auth_header, data=payload)
    result = list()
    result.append(r.status_code)
    if r.status_code != 200:
        result.append(r.json()['validation'][0]['message'])
    return result
