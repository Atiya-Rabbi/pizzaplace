# Generated by Django 2.0.3 on 2020-10-22 16:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_dinner_pasta_regular_salads_sicilian_subs_toppings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('item1', models.CharField(blank=True, max_length=100, null=True)),
                ('item2', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity1', models.IntegerField(blank=True, null=True)),
                ('quantity2', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('username', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
