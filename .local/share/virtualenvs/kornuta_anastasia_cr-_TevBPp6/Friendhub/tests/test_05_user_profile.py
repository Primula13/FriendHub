import requests

from Friendhub.configurations import models
from Friendhub.tools import user_tools

uri = "http://friendhub.dev.cleveroad.com/admin/api/v1/"
token = models.user1.token
password = models.user1.password


def test_01_user_change_password_invalid_new_password(new_passwords_invalid):
    new_password = new_passwords_invalid["new_password"]
    response = user_tools.change_pass_user(password, new_password)
    assert response[0] == new_passwords_invalid["expected_code"]
    assert response[1] == new_passwords_invalid["expected_message"]


def test_02_user_change_password_success():
    new_password = "qwerty11"
    response = user_tools.change_pass_user(new_password, password)
    assert response[0] == 200
    assert user_tools.user_auth(models.user1.email, new_password) == 200
    user_tools.change_pass_user(password, new_password)


def test_03_user_change_password_wrong_old_password():
    auth_header = {"Authorization": token}
    payload = {"password": password, "oldPassword": " " + password}
    r = requests.patch(url=uri + 'users/password', headers=auth_header, data=payload)
    assert r.status_code == 400
    assert r.json()["message"] == "The password you entered is incorrect. Please try again."


def test_04_user_change_pass_permission_admin_token():
    admin_token = models.admin.token
    auth_header = {"Authorization": admin_token}
    payload = {"password": password, "oldPassword": password}
    r = requests.patch(url=uri + 'users/password', headers=auth_header, data=payload)
    assert r.status_code == 401
    assert r.json()["message"] == "You have provided invalid token!"
