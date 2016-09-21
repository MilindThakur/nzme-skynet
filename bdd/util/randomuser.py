# coding=utf-8
from faker import Faker

class RandomUser(object):

    def __init__(self):
        fake = Faker()
        profile = fake.profile()
        self.firstname = profile['name'].split(" ")[0]
        self.lastname = profile['name'].split(" ")[1]
        mail = profile['mail']
        self.email = mail
        self.confirmemail = mail
        self.password = fake.password()
        birthday = profile['birthdate']
        self.birthyear = birthday.split('-')[0]
        self.postcode = profile['ssn']
        self.gender = profile['sex']
