import pytest
from Friendhub.configurations import models


@pytest.fixture(scope="module")
def admin_token():
    return models.admin.token


@pytest.fixture(params=[('download.png', open('/home/kornuta_anastasia_cr/Pictures/Pictures png/download.png',
                        'rb'), 'image/png'),
                        ('melon.jpg', open('/home/kornuta_anastasia_cr/Pictures/melon.jpg', 'rb'),
                        'image/jpg'),
                        ('oranges.png', open('/home/kornuta_anastasia_cr/Pictures/Pictures png/oranges.png', 'rb'),
                         'image/png')]
                )
def valid_images(request):
    return request.param


@pytest.fixture(params=[('0y16.gif', open('/home/kornuta_anastasia_cr/Pictures/0y16.gif', 'rb'), 'image/gif'),
                        ('landscape.jpg', open('/home/kornuta_anastasia_cr/Pictures/landscape.jpg', 'rb'),
                         'image/jpg')])
def invalid_images(request):
    return request.param


@pytest.fixture(params=["A", "Name", "Il-xWxdamNzokFIBiNMG"])
def valid_name(request):
    return request.param

# @pytest.fixture(scope="module")
# def default_admin_profile():
#     auth_header = {"Authorization": models.admin.token}
#     payload = {"firstName": "Admin", "lastName": "Cr"}
#     file = {"file1": ('download.png', open('/home/kornuta_anastasia_cr/Pictures/Pictures png/download.png',
#                                    'rb'), 'image/png')}
#     requests.put(url=uri + 'profile', headers=auth_header, data=payload)
#     requests.patch(url=uri + 'profile/avatar', headers=auth_header, files=file)

@pytest.fixture(scope="module", params=[{
    "case": "New password is empty",
    "new_password": "",
    "old_password": "a123123123",
    "expected_code": 400,
    "expected_message": "Please enter your password."
},
{
    "case": "New password is too short",
    "new_password": "a1231",
    "old_password": "a123123123",
    "expected_code": 400,
    "expected_message": "Password must contain at least 6 characters."
},
{
    "case": "New password is too long",
    "new_password": "ReV9QMXn2EsPpzFlVgANoEgTczIFMepwy37lYOqly",
    "old_password": "a123123123",
    "expected_code": 400,
    "expected_message": "is too long (maximum is 40 characters)"
},
{
    "case": "New password consists of digits only",
    "new_password": "123456",
    "old_password": "a123123123",
    "expected_code": 400,
    "expected_message": "Password must include both numbers and letters."
},
{
    "case": "New password consists of letters only",
    "new_password": "123456",
    "old_password": "a123123123",
    "expected_code": 400,
    "expected_message": "Password must include both numbers and letters."
}])
def new_passwords_admin(request):
    return request.param
