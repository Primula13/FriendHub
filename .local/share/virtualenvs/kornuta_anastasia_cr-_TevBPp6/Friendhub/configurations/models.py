import requests
uri = "http://friendhub.dev.cleveroad.com/api/v1/"
admin_url = uri + 'signin/admin'
user_url = uri + 'signin/basic'


def get_token(role):
    payload = {"email": role.email, "password": role.password}
    r = requests.post(url=role.url, data=payload)
    return r.json()["data"]["session"]["token"]


def profile(role):
    payload = {"email": role.email, "password": role.password}
    r = requests.post(url=role.url, data=payload)
    parsed = r.json()
    return parsed["data"]["user"]


class Admin(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.url = admin_url
        self.token = get_token(self)
        self.profile = profile(self)


class User(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.url = user_url
        self.token = get_token(self)
        self.profile = profile(self)


admin = Admin("admin@gmail.com", "a123123123")
user1 = User("test@gmail.com", "qwerty1")
user2 = User("test1@gmail.com", "qwerty1")
