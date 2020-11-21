from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import BusinessList, BusinessDetail, BusinessSubTypeList, BusinessSubTypeDetail, BusinessTypeList, api_root

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('businesses/', BusinessList.as_view(), name='business-list'),
    path('businesses/<int:pk>/', BusinessDetail.as_view(), name='business-detail'),
    path('business-subtypes/', BusinessSubTypeList.as_view(), name='business-subtype-list'),
    path('business-types/', BusinessTypeList.as_view(), name='business-type-list'),
    path('business-subtypes/<int:pk>/', BusinessSubTypeDetail.as_view(), name='business-subtype-detail'),
])