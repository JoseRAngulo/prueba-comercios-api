from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from .models import Business, BusinessSubType
from .serializers import BusinessSerializer, BusinessSubTypeSerializer, BusinessCreateSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'businesses': reverse('business-list', request=request, format=format),
        'business-sub-types': reverse('business-subtype-list', request=request, format=format)
    })

class BusinessList(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    create_serializer_class = BusinessCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            if hasattr(self, 'create_serializer_class'):
                return self.create_serializer_class

        return super(BusinessList, self).get_serializer_class()
class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessSubTypeList(generics.ListCreateAPIView):
    queryset = BusinessSubType.objects.all()
    serializer_class = BusinessSubTypeSerializer
    
class BusinessSubTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessSubType.objects.all()
    serializer_class = BusinessSubTypeSerializer
