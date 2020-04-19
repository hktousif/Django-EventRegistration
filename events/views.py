from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse, redirect
from .models import *


# Create your views here.
def home_view(request):
    # obj = HomeSlidesModel.objects.all()
    # context = {'slides': obj}
    return render(request, "index.html")


def protocols_view(request):
    # obj = ProtocolsModel.objects.all()
    # context = {'prot': obj.values, }
    return render(request, "protocols.html")


def events_view(request):
    # obj = EventsModel.objects.all()
    # context = {"events": obj}
    return render(request, "events.html")


def about_view(request):
    # obj = AboutModel.objects.all()
    return render(request, "about_ibmr.html")


def gallery_view(request):
    # obj = GalleryModel.objects.all()
    # context = {'gallery': obj}
    return render(request, "gallery.html")


def support_view(request):
    return render(request, "support.html")


@login_required()
def register_view(request):
    if request.method == "POST" and not request.POST.get('edit') == 'edit':
        a = request.POST['College_Name']
        b = request.POST['College_Email_ID']
        c = request.POST['Team_Name']
        d = request.POST['Mob_No']
        e = request.POST['Place']
        x = RegistrationModel(user=request.user, College_Name=a, Team_Name=c, Place=e, College_Email_ID=b, Mob_No=d)
        x.save()
    edit = False
    try:
        obj = RegistrationModel.objects.get(user=request.user)
        if request.POST.get('edit') == 'edit':
            edit = True
    except ObjectDoesNotExist:
        obj = None
    context = {'obj': obj, 'edit': edit}
    return render(request, "register.html", context)
