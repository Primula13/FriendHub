import requests
from Friendhub.configurations import models
from Friendhub.tools import admin_tools

uri = "http://friendhub.dev.cleveroad.com/admin/api/v1/"
token = models.admin.token
password = models.admin.password


def test_01_admin_change_password_invalid_new_password(new_passwords_invalid):
    new_password = new_passwords_invalid["new_password"]
    auth_header = {"Authorization": token}
    payload = {"password": new_password, "oldPassword": password}
    r = requests.patch(url=uri + 'profile/password', headers=auth_header, data=payload)
    if r.status_code == new_passwords_invalid["expected_code"]:
        assert new_passwords_invalid["expected_message"] == r.json()['validation'][0]['message']


def test_02_admin_change_password_wrong_old_password():
    auth_header = {"Authorization": token}
    payload = {"password": password, "oldPassword": " " + password}
    r = requests.patch(url=uri + 'profile/password', headers=auth_header, data=payload)
    assert r.status_code == 400
    assert r.json()["message"] == "The password you entered is incorrect. Please try again."


def test_03_admin_change_password_success():
    auth_header = {"Authorization": token}
    payload = {"password": password, "oldPassword": password}
    r = requests.patch(url=uri + 'profile/password', headers=auth_header, data=payload)
    assert r.status_code == 200
    assert admin_tools.admin_auth(models.admin.email, password)[1] is not None


def test_04_admin_change_password_permission_user_token():
    auth_header = {"Authorization": models.user1.token}
    payload = {"password": password, "oldPassword": password}
    r = requests.patch(url=uri + 'profile/password', headers=auth_header, data=payload)
    assert r.status_code == 401
    assert r.json()["message"] == "You have provided invalid token!"
