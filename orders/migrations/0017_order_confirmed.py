# Generated by Django 2.0.3 on 2020-11-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20201105_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='confirmed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
