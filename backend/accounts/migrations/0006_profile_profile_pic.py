# Generated by Django 4.2.4 on 2023-12-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_full_names_customuser_full_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='avatar.png', upload_to='profile_pics/'),
        ),
    ]