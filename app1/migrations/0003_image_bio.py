# Generated by Django 4.2.11 on 2024-03-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='bio',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
