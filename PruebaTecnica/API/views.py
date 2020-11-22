from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from .models import Business, BusinessSubType, BusinessType
from .serializers import BusinessSerializer, BusinessSubTypeCreateSerializer, BusinessSubTypeSerializer, BusinessCreateSerializer, BusinessTypeSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'businesses': reverse('business-list', request=request, format=format),
        'business-types': reverse('business-type-list', request=request, format=format),
        'business-sub-types': reverse('business-subtype-list', request=request, format=format)
    })

class BusinessList(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessCreateSerializer
class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    create_serializer_class = BusinessCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            if hasattr(self, 'create_serializer_class'):
                return self.create_serializer_class

        return super(BusinessList, self).get_serializer_class()

class BusinessTypeList(generics.ListCreateAPIView):
    queryset = BusinessType.objects.all()
    serializer_class = BusinessTypeSerializer
class BusinessSubTypeList(generics.ListCreateAPIView):
    queryset = BusinessSubType.objects.all()
    serializer_class = BusinessSubTypeSerializer
    create_serializer_class = BusinessSubTypeCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            if hasattr(self, 'create_serializer_class'):
                return self.create_serializer_class

        return super(BusinessSubTypeList, self).get_serializer_class()
    
    
class BusinessSubTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessSubType.objects.all()
    serializer_class = BusinessSubTypeSerializer
