
from django.contrib import admin
from django.urls import path,include #include allows to use other urls from the proj

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',include('lookup.urls')),
]
