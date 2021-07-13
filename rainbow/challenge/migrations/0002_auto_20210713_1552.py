# Generated by Django 3.1.6 on 2021-07-13 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('results', '0001_initial'),
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.region', verbose_name='region'),
        ),
        migrations.AddField(
            model_name='articlechallenge',
            name='main_challenge',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='challenge.challenge', verbose_name='main challenge'),
        ),
    ]
