# Generated by Django 2.1.5 on 2019-02-07 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Scores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batting1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batsman', models.CharField(max_length=255)),
                ('OutType', models.CharField(choices=[('Not Out', 'Not Out'), ('Cought', 'Cought'), ('Bowled', 'Bowled'), ('LBW', 'LBW'), ('Run Out', 'Run Out'), ('Stumped', 'Stumped'), ('Handled the Ball', 'Handled the Ball'), ('Obstructing the Field', 'Obstructing the Field'), ('Retired Hurt', 'Retired Hurt'), ('Other', 'Other')], max_length=255, verbose_name='Out')),
                ('Runs', models.IntegerField(verbose_name='R')),
                ('Bowls', models.IntegerField(verbose_name='B')),
                ('Fours', models.IntegerField(verbose_name='4s')),
                ('Sixes', models.IntegerField(verbose_name='6s')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scores.Score')),
            ],
        ),
    ]
