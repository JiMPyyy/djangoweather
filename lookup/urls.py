
from django.urls import path 
from . import views # . <--- from this directory (lookup)

urlpatterns = [
    path('', views.home, name="home"), #'' IS THE HOME PAGE
    path('about.html', views.about, name="about")
]
