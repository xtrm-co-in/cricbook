from django.contrib import admin
from .models import Batting1,Score
from django.contrib.admin.templatetags.admin_list import date_hierarchy

# Register your models here.
class Batting1Inline(admin.TabularInline):
    classes=('collapse',)
    #Setting Innings as Read Only Field
    #readonly_fields=['mInnings']
    #This is required as unless it won't show mInnings
    fields=('mInnings','Batsman','OutType','Runs','Bowls','Fours','Sixes')
    model=Batting1
    #(self.fields('mInnings').widget).initial_value=1
    extra=1
#    def save_formset(self,request,form,formset,change):
#        instances=formset.save(commit=False)
#        for obj in formset.deleted_objects:
#            obj.delete()
#        for instance in instances:
#            instance.mInnings=1
#            instance.save()
#        formset._save_m2m()
#    def save_model(self,request,obj,form,change):
#        obj.mInnings=1
#        super().save_model(request,obj,form,change)
#    def get_changeform_initial_data(self, request):
#        return {'mInnings': 1}
#    def __init__(self,*args,**kwargs):
#        (self.fields['mInnings'].widget).initial_value=1
#class Batting2Inline(admin.TabularInline):
#    model=Batting1
    #(self.fields('mInnings').widget).initial_value=2
#    extra=1    
class ScoreAdmin(admin.ModelAdmin):
    #save_on_top=True
    date_hierarchy='MatchDate'
    list_filter=['MatchDate']
    search_fields=['mSeries']
    list_display=['MatchDate','Segment','mFormat','mSeries']
    ordering=['-MatchDate']
#    fieldsets=(
#        (None,{'fields':(('MatchDate','Team1'),('Segment','Team2'),('mFormat','mToss'),('mSeries','mHome'),('mGround','mResult'),('mPlace','DLSTrgt'),('mCountry','MOM'))},
#         ('Batting',{'classes':('collapse',),'inlines':['Batting1Inline']}),
#    )
    fields=(('MatchDate','Team1'),('Segment','Team2'),('mFormat','mToss'),('mSeries','mHome'),('mGround','mResult'),('mPlace','DLSTrgt'),('mCountry','MOM'))
    inlines=[Batting1Inline]        
admin.site.register(Score,ScoreAdmin)
admin.site.site_header='CricBook'
admin.site.site_title='Welcome'
admin.site.index_title='CricBook'