from django.contrib import admin
from django.urls import path,include
from fire_noc import views
urlpatterns = [
    path('',views.index,name="index"),
    path("generate_noc/",views.generate_fire_noc_pdf,name="generate_noc"),
]
