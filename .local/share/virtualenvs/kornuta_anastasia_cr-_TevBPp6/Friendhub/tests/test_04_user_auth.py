from Friendhub.tools import user_tools
from Friendhub.configurations import models

credentials = {"right_login": models.user1.email, "right_pass": models.user1.password, "wrong_login": " test@gmail.com",
               "wrong_pass": " qwerty1", "admin_log": models.admin.email, "admin_pass": models.admin.password}

def test_01_user_auth_success():
    response = user_tools.user_auth(credentials["right_login"], credentials["right_pass"])
    assert response[0] == 200
    assert response[1]["data"]["user"] == models.user1.profile

def test_02_user_auth_wrong_login():
    response = user_tools.user_auth(credentials["wrong_login"], credentials["right_pass"])
    assert response[0] == 400
    assert response[1]["validation"][0]["message"] == "Please enter a valid email address."

def test_03_user_auth_wrong_pass():
    response = user_tools.user_auth(credentials["right_login"], credentials["wrong_pass"])
    assert response[0] == 400
    assert response[1]["message"] == "The password you entered is incorrect. Please try again."

def test_04_user_auth_nocreds():
    response = user_tools.user_auth("", "")
    assert response[0] == 400
    assert response[1]["validation"][0]["message"] == "Please enter your password."
    assert response[1]["validation"][1]["message"] == "Please enter a valid email address."

def test_05_user_auth_nopass():
    response = user_tools.user_auth(credentials["right_login"], "")
    assert response[0] == 400
    assert response[1]["validation"][0]["message"] == "Please enter your password."

def test_06_user_auth_nologin():
    response = user_tools.user_auth("", credentials["right_pass"])
    assert response[0] == 400
    assert response[1]["validation"][0]["message"] == "Please enter a valid email address."

def test_07_user_auth_admin_creds():
    response = user_tools.user_auth(credentials["admin_log"], credentials["admin_pass"])
    assert response[0] == 400
    assert response[1]["message"] == "There is no account connected to this email address."
