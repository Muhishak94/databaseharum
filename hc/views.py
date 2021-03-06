from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'hc/index.html')


@login_required(login_url=settings.LOGIN_URL)
def kota(request):
    return render(request, 'hc/kota.html')


@login_required(login_url=settings.LOGIN_URL)
def infopemilu(request):
    return render(request, 'hc/infopemilu.html')
