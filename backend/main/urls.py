from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),

    # Car owners urls 
    path('request_mech/', views.request_mech, name='request_mech'),
    path('req_list/', views.ReqList.as_view(), name='req_list'),
]