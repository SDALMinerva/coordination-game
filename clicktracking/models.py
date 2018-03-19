from django.db import models
from otree.models import Participant, Session
import time

class Click(models.Model):
    participant = models.ForeignKey(Participant)
    timestamp = models.FloatField(default=time.time)
    element = models.CharField(max_length=255)
    page = models.CharField(max_length=255)
    session = models.ForeignKey(Session)

    def __str__(self):
        return "{} {}".format(self.participant.code, self.element)
