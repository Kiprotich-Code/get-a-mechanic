from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import redirect
from django.urls import reverse

from .models import CustomUser, Profile

# Create your signals here 
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(user_logged_in)
def first_login_handler(sender, user, request, **kwargs):
    # Check if user profile is complete 
    if not user.profile.about or not user.profile.full_names:
        update_profile_url = reverse('update_profile')
        return redirect(update_profile_url)