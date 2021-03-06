# Generated by Django 2.2.7 on 2020-05-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_aspirant_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='login_attempts',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='admin',
            name='user_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
