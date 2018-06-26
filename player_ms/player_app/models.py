from django.db import models


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(max_length=2000)
    team_id = models.IntegerField()
    high_score = models.IntegerField()

    def __str__(self):
        return self.name
