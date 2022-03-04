import email
from lib2to3.pgen2.token import AMPER
from sre_parse import State
from types import CoroutineType
from unicodedata import name

from platformdirs import user_cache_dir


class user():
    def __init__(self, name, email, city, state):
        self.name = name
        self.email = email
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.name} lives in {self.city}, {self.state}"

    def Location(self):
        return f"{self.city}, {self.state}"

user1 = user("Anton", "none", "Durnham", "NC")
user2 = user("Cecil", "none", "San Francisco", "CA")

print(user1)
print(user2.Location())


