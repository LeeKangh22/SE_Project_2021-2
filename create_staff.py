# DB test
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from model.models import *

class staff():
    def __init__(self, id, staff_id, staff_pw, name, phone_num, order):
        self.id = id
        self.staff_id = staff_id
        self.staff_pw = staff_pw
        self.name = name
        self.phone_num = phone_num
        self.order = order
    
    def create_staff(self):
        Staff.objects.create(id = self.id,
        staff_id = self.staff_id,
        staff_pw = self.staff_pw,
        name = self.name,
        phone_num = self.phone_num,
        #order = self.order
        )