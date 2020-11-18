from django.contrib import admin
from .models import Business, BusinessType, BusinessSubType

admin.site.register(Business)
admin.site.register(BusinessType)
admin.site.register(BusinessSubType)
# Register your models here.
