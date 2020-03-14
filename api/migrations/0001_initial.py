# Generated by Django 2.2.7 on 2020-03-14 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirant',
            fields=[
                ('aspirant_id', models.AutoField(primary_key=True, serialize=False)),
                ('aspirant_photo', models.ImageField(upload_to='aspirant_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('election_id', models.AutoField(primary_key=True, serialize=False)),
                ('election_name', models.CharField(max_length=100)),
                ('start_timestamp', models.DateTimeField(auto_now_add=True)),
                ('end_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('voter_id', models.AutoField(primary_key=True, serialize=False)),
                ('voter_reg_no', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('voter_password', models.CharField(max_length=255)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.School')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('vote_id', models.AutoField(primary_key=True, serialize=False)),
                ('election_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Election')),
                ('voter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Voter')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=255)),
                ('team_logo', models.ImageField(upload_to='team_logos')),
                ('blockchain_address', models.CharField(max_length=255)),
                ('chairman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chairman_id', to='api.Aspirant')),
                ('election_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Election')),
                ('sec_gen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sec_gen_id', to='api.Aspirant')),
                ('treasurer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treasurer_id', to='api.Aspirant')),
            ],
        ),
        migrations.AddField(
            model_name='aspirant',
            name='voter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Voter'),
        ),
    ]
