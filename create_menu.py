# DB test
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from model.models import *

class menu():
    def __init__(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
    
    def create_staff(self):
        Staff.objects.create(id = self.id,
        id = self.id,
        name = self.name,
        category = self.category,
        price = self.price
        )