# Generated by Django 4.2.4 on 2023-12-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestMech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_owner', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('car_issue', models.TextField()),
                ('priority', models.CharField(max_length=55)),
                ('expected_time', models.IntegerField()),
                ('expected_budget', models.IntegerField()),
                ('mech', models.CharField(max_length=50)),
            ],
        ),
    ]
