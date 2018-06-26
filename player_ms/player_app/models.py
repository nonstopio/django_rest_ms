from django.db import models


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(max_length=2000)
    team_id = models.IntegerField()
    high_score = models.IntegerField()

    def __str__(self):
        return self.name


class PlayerGoal(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match_id = models.IntegerField()
    time = models.TimeField()

    def __str__(self):
        return '%s' % self.id


2931
1
0
2: 35
PM ??         0: 18.38 / Users / nonstopio / workspace / microservices / worldcup / env_worldcup / bin / python3. / match_ms / manage.py
runserver
127.0
.0
.1: 7003
501
2932