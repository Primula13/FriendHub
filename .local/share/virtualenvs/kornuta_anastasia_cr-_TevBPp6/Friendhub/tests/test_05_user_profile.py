import requests

from Friendhub.configurations import models
from Friendhub.tools import user_tools

uri = "http://friendhub.dev.cleveroad.com/admin/api/v1/"
pass_list = [("qwerty1", "qwerty1"), ("qwer1", "a123123123"), ("oankBJfFcnatbB9JLM1VMnQFR8LhmIpUhswuQpU9L",
             "qwerty1"), ("qwerty", "qwerty1"), ("123456", "qwerty1"), ("qwerty1", " qwerty1")]
token = models.user1.token

def test_01_user_change_pass_too_short():
    response = user_tools.change_pass_user(pass_list[1][0], pass_list[1][1])
    assert response[0] == 400
    assert response[1] == "Password must contain at least 6 characters."

def test_02_user_change_pass_too_long():
    response = user_tools.change_pass_user(pass_list[2][0], pass_list[2][1])
    assert response[0] == 400
    assert response[1] == "is too long (maximum is 40 characters)"

def test_03_user_change_pass_digitless():
    response = user_tools.change_pass_user(pass_list[3][0], pass_list[3][1])
    assert response[0] == 400
    assert response[1] == "Password must include both numbers and letters."

def test_04_user_change_pass_only_digits():
    response = user_tools.change_pass_user(pass_list[4][0], pass_list[4][1])
    assert response[0] == 400
    assert response[1] == "Password must include both numbers and letters."

def test_05_user_change_pass_success():
    response = user_tools.change_pass_user(pass_list[0][0], pass_list[0][1])
    assert response[0] == 200
    assert user_tools.user_auth(models.user1.email, pass_list[0][0]) == 200

def test_06_user_change_pass_wrongpass():
    auth_header = {"Authorization": token}
    payload = {"password": pass_list[5][0], "oldPassword": pass_list[5][1]}
    r = requests.patch(url=uri + 'users/password', headers=auth_header, data=payload)
    assert r.status_code == 400
    assert r.json()["message"] == "The password you entered is incorrect. Please try again."

def test_07_user_change_pass_permission_admin_token():
    admin_token = models.admin.token
    auth_header = {"Authorization": admin_token}
    payload = {"password": pass_list[0][0], "oldPassword": pass_list[0][1]}
    r = requests.patch(url=uri + 'users/password', headers=auth_header, data=payload)
    assert r.status_code == 401
    assert r.json()["message"] == "You have provided invalid token!"
