from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('user_home/', views.user_home, name='user_home'),

    # Car owners urls 
    path('request_mech/<mech_id>', views.request_mech, name='request_mech'),
    path('req_list/', views.ReqList.as_view(), name='req_list'),
    path('req_details/<int:pk>', views.ReqDetails.as_view(), name='req_details'),

    # list mechanics
    path('mech_list/', views.mech_list, name='mech_list'),
]
