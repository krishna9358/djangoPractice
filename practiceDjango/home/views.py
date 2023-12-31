from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    # return HttpResponse("Hello World!")
    return render(request, 'home/index.html', {'today': datetime.today})


@login_required(login_url='/admin')
def authorize(request):
    return render(request, 'home/authorize.html',{})
