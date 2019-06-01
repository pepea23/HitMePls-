# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
class LandingPageView(View):
    def get(self,reuest):
        return HttpResponse('<form action = "." method ="post"><input type ="email" /> <button type ="submit" >Sunbmit </button> </form>')