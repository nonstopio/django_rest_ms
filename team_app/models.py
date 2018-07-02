from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    logo = models.ImageField(max_length=2000)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
