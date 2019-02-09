# Generated by Django 2.1.5 on 2019-02-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MatchDate', models.DateField(verbose_name='Match Date')),
                ('Segment', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], max_length=255)),
                ('mFormat', models.CharField(choices=[('T10', 'T10'), ('T20', 'T20'), ('ODI', 'ODI'), ('Test', 'Test')], max_length=255, verbose_name='Format')),
                ('mSeries', models.CharField(max_length=255, verbose_name='Series')),
                ('mGround', models.CharField(max_length=255, verbose_name='Ground')),
                ('mPlace', models.CharField(max_length=255, verbose_name='Place')),
                ('mCountry', models.CharField(max_length=255, verbose_name='Country')),
                ('Team1', models.CharField(max_length=255, verbose_name='Team-1')),
                ('Team2', models.CharField(max_length=255, verbose_name='Team-2')),
                ('mToss', models.CharField(max_length=255, verbose_name='Toss')),
                ('mHome', models.CharField(max_length=255, verbose_name='Home Pitch')),
                ('mResult', models.CharField(max_length=255, verbose_name='Result')),
                ('DLSTrgt', models.CharField(blank=True, max_length=255, verbose_name='DLS Target')),
                ('MOM', models.CharField(max_length=255, verbose_name='Man of the Match')),
            ],
        ),
    ]