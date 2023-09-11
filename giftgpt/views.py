from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import giftgptapi

def home(request):
    return render(request,'home.html')

def gift(request):
    if request.method == "GET":
        redirect('/')
    else:
        respuesta = giftgptapi.GiftAI(request.POST['name'],request.POST['trela'],request.POST['age'],request.POST['intrests'],request.POST['story'],request.POST['status'])

        return render(request,'gift.html', {
            'respuesta': respuesta
        })
