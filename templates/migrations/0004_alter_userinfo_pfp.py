# Generated by Django 5.0.1 on 2024-05-07 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0003_userinfo_originalname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='pfp',
            field=models.ImageField(blank=True, upload_to='astral/files/pfp'),
        ),
    ]
