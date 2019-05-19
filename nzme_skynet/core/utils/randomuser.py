# coding=utf-8
from faker import Faker


class RandomUser(object):

    def __init__(self):
        self.fake = Faker()
        self._profile = self.fake.profile()
        self.FIRSTNAME = None
        self.LASTNAME = None
        self.EMAIL = None
        self.PASSWORD = None
        self.BIRTHDAY = None
        self.POSTCODE = None
        self.GENDER = None

    def create_user(self):
        self.FIRSTNAME = self._profile['name'].split(" ")[0]
        self.LASTNAME = self._profile['name'].split(" ")[1]
        mail = self._profile['mail']
        self.EMAIL = mail
        self.PASSWORD = self.fake.password()
        birthday = self._profile['birthdate']
        self.BIRTHYEAR = str(self._profile['birthdate'].year)
        self.POSTCODE = self.fake.postcode()
        self.GENDER = self._profile['sex']
