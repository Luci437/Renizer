# Generated by Django 3.0.6 on 2020-05-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saloonapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HairStyles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('style_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
