from django.urls import path 
from . import views

urlpatterns = [
    path('user/signup/', views.register_user, name='register_user'),
    path('mech/signup/', views.register_mech, name='register_mech'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # profile
    path('update_profile/', views.update_profile, name='update_profile'),
    path('view_profile/ <user_id>', views.view_profile, name='view_profile'),
]
