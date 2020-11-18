from rest_framework import serializers
from .models import Business, BusinessSubType, BusinessType

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class BusinessSubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessSubType
        fields = '__all__'

class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = '__all__'