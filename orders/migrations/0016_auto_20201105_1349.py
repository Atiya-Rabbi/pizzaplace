# Generated by Django 2.0.3 on 2020-11-05 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20201103_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmedorders',
            name='status',
            field=models.CharField(choices=[('Your food is getting ready', '1'), ('Out for Delivery', '2'), ('Delivered', '3'), ('Invalid Order', '4')], default='Your food is getting ready', max_length=100),
        ),
    ]
