# Generated by Django 3.1.2 on 2020-10-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyFacebook', '0006_auto_20201022_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='Username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
