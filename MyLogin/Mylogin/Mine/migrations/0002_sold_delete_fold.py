# Generated by Django 4.1.5 on 2023-02-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('ltext', models.CharField(max_length=20000)),
                ('slug', models.SlugField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Fold',
        ),
    ]