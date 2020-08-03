from django.contrib import admin
from django.urls import path,include
from .views import QueryView
from rest_framework import routers
router = routers.DefaultRouter()
router.register("queries",QueryView)
urlpatterns = [
    path('',include(router.urls))
]