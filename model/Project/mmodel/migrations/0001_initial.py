# Generated by Django 4.1.5 on 2023-02-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('des', models.CharField(max_length=300)),
            ],
        ),
    ]
