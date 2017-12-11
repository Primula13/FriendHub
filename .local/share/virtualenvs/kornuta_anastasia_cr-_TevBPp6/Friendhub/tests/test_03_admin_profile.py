import requests
from Friendhub.configurations import models

uri = "http://friendhub.dev.cleveroad.com/admin/api/v1/"


def test_01_admin_change_avatar_success(admin_token, valid_images):
    auth_header = {"Authorization": admin_token}
    old_img = models.admin.profile["avatar"]["original"]
    file = {"avatar": valid_images}
    r = requests.patch(url=uri + 'profile/avatar', headers=auth_header, files=file)
    assert r.status_code == 200
    assert r.json()["data"]["avatar"]["original"] != old_img
    assert r.json()["data"]["avatar"]["original"] is not None


def test_02_admin_change_avatar_fail(admin_token, invalid_images):
    auth_header = {"Authorization": admin_token}
    file = {"avatar": invalid_images}
    r = requests.patch(url=uri + 'profile/avatar', headers=auth_header, files=file)
    assert r.status_code == 400


def test_03_admin_change_firstname_success(admin_token, valid_name):
    old_fname = models.admin.profile["firstName"]
    auth_header = {"Authorization": admin_token}
    payload = {"firstName": valid_name, "lastName": models.admin.profile["lastName"]}
    r = requests.put(url=uri + 'profile', headers=auth_header, data=payload)
    assert r.status_code == 200
    assert old_fname != r.json()["data"]["firstName"]
    assert r.json()["data"]["firstName"] is not None


def test_04_admin_change_lastname_success(admin_token, valid_name):
    old_lname = models.admin.profile["lastName"]
    auth_header = {"Authorization": admin_token}
    payload = {"firstName": models.admin.profile["firstName"], "lastName": valid_name}
    r = requests.put(url=uri + 'profile', headers=auth_header, data=payload)
    assert r.status_code == 200
    assert old_lname != r.json()["data"]["lastName"]
    assert r.json()["data"]["lastName"] is not None


def test_05_admin_change_firstname_fail_empty(admin_token):
    auth_header = {"Authorization": admin_token}
    payload = {"firstName": "", "lastName": models.admin.profile["lastName"]}
    r = requests.put(url=uri + 'profile', headers=auth_header, data=payload)
    assert r.status_code == 400
    assert r.json()["validation"][0]["message"] == "must not be empty"
    assert r.json()["validation"][1]["message"] == "Minimum field length is 1."


def test_06_admin_change_firstname_fail_toolong(admin_token):
    auth_header = {"Authorization": admin_token}
    payload = {"firstName": "6Q90RP61F7DB3nfVju5AR", "lastName": models.admin.profile["lastName"]}
    r = requests.put(url=uri + 'profile', headers=auth_header, data=payload)
    assert r.status_code == 400
    assert r.json()["validation"][0]["message"] == "Maximum field length is 20."


def test_07_admin_change_lastname_fail_empty(admin_token):
    auth_header = {"Authorization": admin_token}
    payload = {"firstName": models.admin.profile["firstName"], "lastName": ""}
    r = requests.put(url=uri + 'profile', headers=auth_header, data=payload)
    assert r.status_code == 400
    assert r.json()["validation"][0]["message"] == "must not be empty"
    assert r.json()["validation"][1]["message"] == "Minimum field length is 1."


def test_08_admin_change_lastname_fail_toolong(admin_token):
    auth_header = {"Authorization": admin_token}
    payload = {"firstName": models.admin.profile["firstName"], "lastName": "6Q90RP61F7DB3nfVju5AR"}
    r = requests.put(url=uri + 'profile', headers=auth_header, data=payload)
    assert r.status_code == 400
    assert r.json()["validation"][0]["message"] == "Maximum field length is 20."


def test_09_admin_change_name_usrtoken():
    auth_header = {"Authorization": models.user1.token}
    payload = {"firstName": models.admin.profile["firstName"], "lastName": models.admin.profile["lastName"]}
    r = requests.put(url=uri + 'profile', headers=auth_header, data=payload)
    assert r.status_code == 401
    assert r.json()["message"] == "You have provided invalid token!"
