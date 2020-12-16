# Generated by Django 3.1.4 on 2020-12-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='URL')),
                ('url_status', models.CharField(db_index=True, max_length=30, verbose_name='URL status')),
            ],
        ),
    ]
