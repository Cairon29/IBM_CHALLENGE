from django.contrib import admin
from django.urls import path
from hf_models.views import *
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home)
]
