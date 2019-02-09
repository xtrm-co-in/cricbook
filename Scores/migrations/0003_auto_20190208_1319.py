# Generated by Django 2.1.5 on 2019-02-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scores', '0002_batting1'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='mInnings',
            field=models.SmallIntegerField(default=1, verbose_name='Innings'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='score',
            name='MOM',
            field=models.CharField(blank=True, max_length=255, verbose_name='Man of the Match'),
        ),
    ]
