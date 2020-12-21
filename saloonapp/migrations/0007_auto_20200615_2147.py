# Generated by Django 3.0.6 on 2020-06-15 16:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saloonapp', '0006_auto_20200531_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalpay', models.IntegerField(default=0)),
                ('billingdate', models.DateField(default=datetime.datetime(2020, 6, 15, 21, 47, 33, 887716))),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saloonapp.LoginInfo')),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 15, 21, 47, 33, 884714)),
        ),
        migrations.CreateModel(
            name='BillingCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=200)),
                ('cardnumber', models.IntegerField(default=0)),
                ('cardcvv', models.IntegerField(default=0)),
                ('cardexp', models.CharField(max_length=100)),
                ('billingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saloonapp.Billing')),
            ],
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('pincode', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('billingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saloonapp.Billing')),
            ],
        ),
    ]