# Generated by Django 3.1.6 on 2021-09-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_is_lgbt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_lgbt',
        ),
        migrations.AddField(
            model_name='user',
            name='is_lgbtqia',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no'), ('prefer_not_to_say', 'prefer not to say')], max_length=255, null=True, verbose_name='Do you consider yourself LGBTQIA+?'),
        ),
    ]
