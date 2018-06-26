from django.db import models


class Match(models.Model):
    id = models.AutoField(primary_key=True)
    team_a_id = models.IntegerField()
    team_b_id = models.IntegerField()
    venue = models.CharField(max_length=500)
    start_time = models.DateTimeField()

    def __str__(self):
        return '%s vs %s' % (
            self.team_a_id,
            self.team_b_id
        )
