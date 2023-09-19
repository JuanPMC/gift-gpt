from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home),
    path('gift',views.gift),
    path('three-simple-steps-to-effortless-gift-shopping-with-the-amazon-gift-finder-ai',views.blog_step),
    path('top-10-reasons-to-embrace-the-amazon-gift-finder-ai',views.blog_top),
]
