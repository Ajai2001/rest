from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class personview(viewsets.ModelViewSet):
    queryset = person.objects.all()
    serializer_class = personform
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]