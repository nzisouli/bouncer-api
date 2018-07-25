# Generated by Django 2.0.7 on 2018-07-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('blacklist', '0002_auto_20180725_1038'), ('blacklist', '0003_remove_emailhostentry_lower_case_entry_value'), ('blacklist', '0004_emailhostentry_lower_case_entry_value')]

    dependencies = [
        ('blacklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('entry_value', models.EmailField(max_length=254)),
                ('lower_case_entry_value', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailHostEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('entry_value', models.CharField(max_length=254)),
                ('lower_case_entry_value', models.CharField(default='example.com', max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IPEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('entry_value', models.GenericIPAddressField()),
                ('lower_case_entry_value', models.GenericIPAddressField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Email_Entry',
        ),
        migrations.DeleteModel(
            name='Host_Entry',
        ),
        migrations.DeleteModel(
            name='IP_Entry',
        ),
    ]
