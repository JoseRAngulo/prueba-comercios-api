from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from .models import Business, BusinessSubType
from .serializers import BusinessSerializer, BusinessSubTypeSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'businesses': reverse('business-list', request=request, format=format),
        'business-sub-types': reverse('business-subtype-list', request=request, format=format)
    })

class BusinessList(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessSubTypeList(generics.ListCreateAPIView):
    queryset = BusinessSubType.objects.all()
    serializer_class = BusinessSubTypeSerializer
    
class BusinessSubTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessSubType.objects.all()
    serializer_class = BusinessSubTypeSerializer
