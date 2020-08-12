
from django.db import models


class Postt(models.Model):
    title = models.CharField(max_length=455)
    desc = models.CharField(max_length=1045)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Poste