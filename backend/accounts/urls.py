from django.urls import path 
from . import views

urlpatterns = [
    path('user/signup/', views.register_user, name='register_user'),
    path('mech/signup/', views.register_mech, name='register_mech'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logout_user, name='logout'),
]