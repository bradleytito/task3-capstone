from django.db import models

class Endorser(models.Model):
    """This class is used to track the names and surnames of all endorsers."""

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        """This method will be used to return the name and surname of a specific endorser saved in the database."""
        return f'{self.name} {self.surname}'