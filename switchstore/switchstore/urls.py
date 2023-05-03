from django.contrib import admin
from django.urls import path
from django.urls import include
from app_main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]
