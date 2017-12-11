from Friendhub.tools import admin_tools
from Friendhub.configurations import models

credentials = {"right_log": "admin@gmail.com", "right_pass": "a123123123", "wrong_log": " admin@gmail.com",
               "wrong_pass": " a123123123", "user_log": models.user1.email, "user_pass": models.user1.password}


def test_01_admin_auth_success():
    response = admin_tools.admin_auth(credentials["right_log"], credentials["right_pass"])
    assert response[0] == 200
    assert response[1]["data"]["user"] == models.admin.profile


def test_02_admin_auth_wrong_login():
    response = admin_tools.admin_auth(credentials["wrong_log"], credentials["right_pass"])
    assert response[0] == 400
    assert response[1]["validation"][0]["message"] == "Please enter a valid email address."


def test_03_admin_auth_wrong_pass():
    response = admin_tools.admin_auth(credentials["right_log"], credentials["wrong_pass"])
    assert response[0] == 400
    assert response[1]["message"] == "The password you entered is incorrect. Please try again."


def test_04_admin_auth_nocreds():
    response = admin_tools.admin_auth("", "")
    assert response[0] == 400
    assert response[1]["validation"][0]["message"] == "Please enter your password."
    assert response[1]["validation"][3]["message"] == "Please enter a valid email address."


def test_05_admin_auth_nopass():
    response = admin_tools.admin_auth(credentials["right_log"], "")
    assert response[0] == 400
    assert response[1]["validation"][0]["message"] == "Please enter your password."


def test_06_admin_auth_nologin():
    response = admin_tools.admin_auth("", credentials["right_pass"])
    assert response[0] == 400
    assert response[1]["validation"][0]["message"] == "Please enter a valid email address."


def test_07_admin_auth_usr_creds():
    response = admin_tools.admin_auth(credentials["user_log"], credentials["user_pass"])
    assert response[0] == 400
    assert response[1]["message"] == "There is no account connected to this email address."
