# Generated by Django 5.1.6 on 2025-03-11 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountinfo',
            old_name='phone',
            new_name='phoneNumber',
        ),
        migrations.RenameField(
            model_name='accountinfo',
            old_name='profile_image',
            new_name='profileImage',
        ),
        migrations.RenameField(
            model_name='accountinfo',
            old_name='user_name',
            new_name='userName',
        ),
    ]
