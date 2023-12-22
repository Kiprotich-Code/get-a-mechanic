# Generated by Django 4.2.4 on 2023-12-21 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='about',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='location',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_no',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.IntegerField()),
                ('about', models.TextField(blank=True, max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]