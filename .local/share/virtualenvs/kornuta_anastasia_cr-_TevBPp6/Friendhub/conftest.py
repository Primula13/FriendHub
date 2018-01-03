import pytest


@pytest.fixture(scope="session", params=[('download.png',
                open('/home/kornuta_anastasia_cr/Pictures/Pictures png/download.png', 'rb'), 'image/png'),
                        ('melon.jpg', open('/home/kornuta_anastasia_cr/Pictures/melon.jpg', 'rb'), 'image/jpg'),
                        ('oranges.png', open('/home/kornuta_anastasia_cr/Pictures/Pictures png/oranges.png', 'rb'),
                         'image/png')])
def valid_images(request):
    return request.param


@pytest.fixture(scope="session", params=[('0y16.gif', open('/home/kornuta_anastasia_cr/Pictures/0y16.gif', 'rb'),
                                          'image/gif'),
                ('landscape.jpg', open('/home/kornuta_anastasia_cr/Pictures/landscape.jpg', 'rb'), 'image/jpg')])
def invalid_images(request):
    return request.param


@pytest.fixture(scope="session", params=["A", "Name", "Il-xWxdamNzokFIBiNMG"])
def valid_name(request):
    return request.param


@pytest.fixture(scope="session", params=[
    {
        "case": "Name field is empty",
        "name": "",
        "expected_message": "must not be empty"
    },
    {
        "case": "Name is too long",
        "name": "6Q90RP61F7DB3nfVju5AR",
        "expected_message": "Maximum field length is 20."
    }])
def invalid_name(request):
    return request.param


@pytest.fixture(scope="session", params=[
    {
        "case": "New password is empty",
        "new_password": "",
        "expected_code": 400,
        "expected_message": "Please enter your password."
    },
    {
        "case": "New password is too short",
        "new_password": "a1231",
        "expected_code": 400,
        "expected_message": "Password must contain at least 6 characters."
    },
    {
        "case": "New password is too long",
        "new_password": "ReV9QMXn2EsPpzFlVgANoEgTczIFMepwy37lYOqly",
        "expected_code": 400,
        "expected_message": "is too long (maximum is 40 characters)"
    },
    {
        "case": "New password consists of digits only",
        "new_password": "123456",
        "expected_code": 400,
        "expected_message": "Password must include both numbers and letters."
    },
    {
        "case": "New password consists of letters only",
        "new_password": "123456",
        "expected_code": 400,
        "expected_message": "Password must include both numbers and letters."
    }])
def new_passwords_invalid(request):
    return request.param


@pytest.fixture(scope="session", params=[
    {
        "firstName": "A",
        "gender": 1,
        "birthday": "2004-03-28T07:15:58.755Z",
        "country": "USA",
        "about": "A"
    },
    {
        "firstName": "iHN0U8OiigET8GbKYCIg",
        "gender": 2,
        "birthday": "1990-12-12T07:15:58.755Z",
        "country": "USA",
        "about": "s2AiUD4zK1rPQGCQVf52q119xvJN7L2OO7gvPTi5LtEwnpTy2HFJeysjhDWsbHaNTZtrmC f13tO sJ5LAhw1pNv6nIg" +
                 "E0URLCCSsuRiZQ32Y0BncPA8pbrCOWTb9Rwnq3Z A7oM79aiJOChUEJOmdy7W0U0QCzrtmucX Slh1F MRlteUHoIN5nNVcLqr" +
                 "ChLLps1AO 6OKjI0VsPk4VBWfFY9MvumRkOIS ZUVjR3HlHSywFqs8lmDT184asO2QWNQgfpRUaQaA79JKyWFMCxtQr6h5OYEoM" +
                 "gw8KMkVTIcBNjFRSHYgp6pHcE z4TdlLcjRbkhLcyFzO55Td6n1tdnQpulzzooSM9fTpXRv uHunbCDWKMEbVfMGtYAueVY5ZC" +
                 "K1IdEeXvElkEY"
    },
    {
        "firstName": "Test",
        "gender": 2,
        "birthday": "1920-12-12T07:15:58.755Z",
        "country": "Canada",
        "about": ""
    }
])
def valid_user_data(request):
    return request.param
