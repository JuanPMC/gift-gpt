from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import giftgptapi

def home(request):
    return render(request,'home.html')

def gift(request):
    if request.method == "GET":
        redirect('/')
    else:
        # respuesta = giftgptapi.GiftAI(request.POST['name'],request.POST['trela'],request.POST['age'],request.POST['intrests'],request.POST['story'],request.POST['status'])
        # plantilla = 'gift.html'

        plantilla = 'giftSeveral.html'
        respuesta1 = giftgptapi.GiftAI(request.POST['name'],request.POST['trela'],request.POST['age'],request.POST['intrests'],request.POST['story'],request.POST['status'])
        respuesta = respuesta1.arr

        return render(request,plantilla, {
            'gifts': respuesta
        })

def blog_top(request):
    return render(request,"blog-top10.html")
def blog_step(request):
    return render(request,"blog-step.html")
