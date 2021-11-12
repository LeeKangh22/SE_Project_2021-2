# DB test
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from model.models import *

hojun = Staff.objects.get(id = 1)

print(hojun.phone_num)
    