from django.shortcuts import render
from .models import Queries
from rest_framework import viewsets
from .serilizer import serilizer


class QueryView(viewsets.ModelViewSet):
    queryset = Queries.objects.all()
    serializer_class = serilizer