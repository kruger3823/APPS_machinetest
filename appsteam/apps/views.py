from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,reverse
from . import models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.core.mail import send_mail

from .models import mark



def results_1(request):
    if request.method=="POST":

        data = request.POST['date']
        data1 = request.POST['num']
        print(data)
        date2=str(data)
        cr = mark.objects.filter(date=date2,register=data1)
        return render(request,"apps/results.html",{'cr':cr})
    return render(request,"apps/results.html")

