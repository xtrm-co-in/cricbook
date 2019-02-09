from django.shortcuts import render
from .models import Score

# Create your views here.
def index(Request):
	latest_match_list=Score.objects.order_by('-MatchDate')
	context={'latest_match_list':latest_match_list,}
	return render(Request,'scores/index.html',context)
