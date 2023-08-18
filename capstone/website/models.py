from django.db import models

class Endorser(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.surname}'