# Generated by Django 2.0.7 on 2018-07-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blacklist", "0002_auto_20180727_1042")]

    operations = [
        migrations.AddField(
            model_name="emailentry",
            name="hashed_value",
            field=models.CharField(default="hash", max_length=254),
            preserve_default=False,
        )
    ]