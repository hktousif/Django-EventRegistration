# Generated by Django 2.0.7 on 2020-03-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_contactmodel_homeslidesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='Email_ID',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='homeslidesmodel',
            name='About_1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homeslidesmodel',
            name='About_2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homeslidesmodel',
            name='About_3',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
