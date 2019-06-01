# Create your views here.
from .models import Hitter
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class LandingPageView(View):
    def get(self,request):
        return render(
            request,
            'index.html'
        )
    def post(self,request):
        email = request.POST['email']

        Hitter.objects.create(email=email)
        return HttpResponse()