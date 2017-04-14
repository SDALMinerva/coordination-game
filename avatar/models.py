from django.db import models

author = 'Brian J. Goode'

doc = """
Manage User Avatars in oTree
"""


class Avatar(models.Model):
    name = models.CharField(max_length = 100);
    src = models.URLField()
