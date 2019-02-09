from django.db import models
from datetime import date

# Create your models here.
class Score(models.Model):
    T10='T10'
    T20='T20'
    ODI='ODI'
    Tests='Test'
    Men='Men'
    Women='Women'
    SegmentChoices=((Men,'Men'),(Women,'Women'),)
    FormatChoices=((T10,'T10'),(T20,'T20'),(ODI,'ODI'),(Tests,'Test'),)
    MatchDate=models.DateField('Match Date',default=date.today())
    Segment=models.CharField(max_length=255,choices=SegmentChoices,)
    mFormat=models.CharField('Format',max_length=255,choices=FormatChoices,)
    mSeries=models.CharField('Series',max_length=255,)
    mGround=models.CharField('Ground',max_length=255,)
    mPlace=models.CharField('Place',max_length=255,)
    mCountry=models.CharField('Country',max_length=255,)
    Team1=models.CharField('Team-1',max_length=255,)
    Team2=models.CharField('Team-2',max_length=255,)
    mToss=models.CharField('Toss',max_length=255,)
    mHome=models.CharField('Home Pitch',max_length=255,)
    mResult=models.CharField('Result',max_length=255,)
    DLSTrgt=models.CharField('DLS Target',max_length=255,blank=True,)
    MOM=models.CharField('Man of the Match',max_length=255,blank=True)
    def __str__(self):
        return '%s (%s - %s %s)' % (self.mSeries,self.Segment,self.mPlace,self.mFormat)
    
class Batting1(models.Model):
    NotOut='Not Out'
    Cought='Cought'
    Bowled='Bowled'
    LBW='LBW'
    RunOut='Run Out'
    Stumped='Stumped'
    Handled='Handled the Ball'
    Obstruct='Obstructing the Field'
    Retired='Retired Hurt'
    Othr='Other'
    OutChoices=((NotOut,'Not Out'),(Cought,'Cought'),(Bowled,'Bowled'),(LBW,'LBW'),(RunOut,'Run Out'),(Stumped,'Stumped'),(Handled,'Handled the Ball'),(Obstruct,'Obstructing the Field'),(Retired,'Retired Hurt'),(Othr,'Other'),)
    score=models.ForeignKey(Score,on_delete=models.CASCADE)
    mInnings=models.SmallIntegerField('Innings')
    Batsman=models.CharField(max_length=255)
    OutType=models.CharField('Out',max_length=255,choices=OutChoices,)
    Runs=models.IntegerField('R')
    Bowls=models.IntegerField('B')
    Fours=models.IntegerField('4s')
    Sixes=models.IntegerField('6s')
    def __str__(self):
        return '%s' % (self.Batsman)