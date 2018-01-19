from django.db import models


class Programmer(models.Model):
    username = models.CharField(max_length=120)
    phone_no = models.CharField(max_length=20)
    # country = models.CharField(choices=['a', 'b'])

    def __str__(self):
        return self.username
