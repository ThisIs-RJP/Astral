# Generated by Django 5.0.1 on 2024-05-07 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0002_alter_userinfo_email_alter_userinfo_fname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='originalName',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
