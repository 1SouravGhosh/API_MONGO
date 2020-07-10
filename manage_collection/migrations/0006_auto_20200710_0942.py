# Generated by Django 3.0.5 on 2020-07-10 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_schedule', '0001_initial'),
        ('manage_collection', '0005_auto_20200709_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='schedule',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='manage_schedule.Schedule'),
        ),
    ]
