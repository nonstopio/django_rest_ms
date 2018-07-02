# Generated by Django 2.0.6 on 2018-06-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('team_a_id', models.IntegerField()),
                ('team_b_id', models.IntegerField()),
                ('venue', models.CharField(max_length=500)),
                ('start_time', models.DateTimeField()),
            ],
        ),
    ]