# Generated by Django 2.0.7 on 2020-04-19 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20200419_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='Team_Name',
            field=models.CharField(default='Null', max_length=30),
            preserve_default=False,
        ),
    ]
