import requests
from Friendhub.configurations import models

uri = "http://friendhub.dev.cleveroad.com/api/v1/"
token = models.user1.token


def test_01_user_change_profile_success(valid_user_data):
    header = {"Content-Type": "application/json", "Authorization": token}
    payload = {"firstName": valid_user_data["firstName"], "gender": valid_user_data["gender"],
               "birthday": valid_user_data["birthday"], "country": valid_user_data["country"],
               "about": valid_user_data["about"]}
    r = requests.patch(url=uri + "users/profile", headers=header, data=payload)
    assert r.status_code == 200
    assert r.json() is not None
