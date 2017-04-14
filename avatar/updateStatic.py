import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import django
django.setup()

from avatar.models import Avatar

img_list = os.listdir('static/avatar/')

for img in img_list:
    name = img.split('.')[0]
    src = img
    Avatar.objects.get_or_create(name = name, src = src)
