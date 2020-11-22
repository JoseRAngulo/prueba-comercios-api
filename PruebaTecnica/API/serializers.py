from rest_framework import serializers
from .models import Business, BusinessSubType, BusinessType

class BusinessSerializer(serializers.ModelSerializer):
    types = serializers.StringRelatedField(many=True)
    class Meta:
        model = Business
        fields = ['id', 'name', 'date', 'owner_name', 'address', 'types']

class BusinessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class BusinessSubTypeSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField(many=False)
    class Meta:
        model = BusinessSubType
        fields = ['id', 'description', 'type']

class BusinessSubTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessSubType
        fields = '__all__'
class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = '__all__'