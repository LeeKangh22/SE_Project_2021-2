import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from model.models import *

lists = Stock.objects.all()
print(lists)