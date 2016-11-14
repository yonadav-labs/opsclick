from __future__ import unicode_literals

from django.db import models

class OpsUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    genre = models.CharField(max_length=10)
    experience = models.IntegerField(default=0)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resume', null=True, blank=True)
    verified = models.BooleanField(default=False)
    vkey = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

