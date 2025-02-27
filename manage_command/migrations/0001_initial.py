# Generated by Django 3.0.5 on 2020-07-07 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manage_collection', '0002_auto_20200707_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Command', models.CharField(blank=True, max_length=50)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='manage_collection.Collection')),
            ],
            options={
                'verbose_name': 'command',
                'verbose_name_plural': 'commands',
            },
        ),
    ]
