# Generated by Django 4.2.5 on 2023-09-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('species', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=240)),
            ],
        ),
    ]
