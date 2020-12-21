# Generated by Django 3.0.6 on 2020-06-15 16:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saloonapp', '0007_auto_20200615_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='billingdate',
            field=models.DateField(default=datetime.datetime(2020, 6, 15, 22, 1, 57, 490473)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 15, 22, 1, 57, 486471)),
        ),
        migrations.CreateModel(
            name='BillingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saloonapp.Billing')),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saloonapp.Product')),
            ],
        ),
    ]
