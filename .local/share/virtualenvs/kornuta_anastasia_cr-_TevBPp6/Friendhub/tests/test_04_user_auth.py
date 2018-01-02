from Friendhub.tools import user_tools
from Friendhub.configurations import models

credentials = {"right_login": models.user1.email, "right_password": models.user1.password,
               "wrong_login": " test@gmail.com", "wrong_password": " qwerty1",
               "admin_login": models.admin.email, "admin_password": models.admin.password}


def test_01_user_auth_success():
    response = user_tools.user_auth(credentials["right_login"], credentials["right_password"])
    assert response[0] == 200
    assert response[1]["data"]["user"] == models.user1.profile


def test_02_user_auth_wrong_login():
    response = user_tools.user_auth(credentials["wrong_login"], credentials["right_password"])
    assert response[0] == 400
    assert response[1]["validation"][0]["message"] == "Please enter a valid email address."


def test_03_user_auth_wrong_pass():
    response = user_tools.user_auth(credentials["right_login"], credentials["wrong_password"])
    assert response[0] == 400
    assert response[1]["message"] == "The password you entered is incorrect. Please try again."


def test_04_user_auth_nocreds():
    response = user_tools.user_auth("", "")
    assert response[0] == 400
    assert response[1]["validation"][0]["message"] == "Please enter your password."
    assert response[1]["validation"][1]["message"] == "Please enter a valid email address."


def test_05_user_auth_admin_creds():
    response = user_tools.user_auth(credentials["admin_login"], credentials["admin_password"])
    assert response[0] == 400
    assert response[1]["message"] == "There is no account connected to this email address."
