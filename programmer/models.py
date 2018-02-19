from django.db import models


class Programmer(models.Model):
    username = models.CharField(max_length=120)
    phone_no = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)
    # country = models.CharField(choices=['a', 'b'])

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return '/'

