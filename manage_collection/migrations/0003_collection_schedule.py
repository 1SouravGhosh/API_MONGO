# Generated by Django 3.0.5 on 2020-07-08 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_schedule', '0001_initial'),
        ('manage_collection', '0002_auto_20200707_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='manage_schedule.Schedule'),
        ),
    ]
