# Generated by Django 3.0.6 on 2020-07-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200510_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendGrid',
            fields=[
                ('key_id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.TextField()),
            ],
        ),
    ]