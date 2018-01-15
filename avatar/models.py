from django.db import models

from random import shuffle

author = 'Brian J. Goode'

doc = """
Manage User Avatars in oTree
"""


class Avatar(models.Model):
    name = models.CharField(max_length = 100)
    src = models.URLField()

    def __str__(self):
        return self.src

    @classmethod
    def randAvatars(self,n=None):
        avatars = self._meta.model.objects.all()
        pk_list = list(range(1,len(avatars)))    
        shuffle(pk_list)
        
        if n:
            pk_list = pk_list[:n]    

        objects = dict([(obj.id, obj) for obj in avatars])
        sorted_objects = [avatars[id] for id in pk_list]
        
        return iter(sorted_objects)