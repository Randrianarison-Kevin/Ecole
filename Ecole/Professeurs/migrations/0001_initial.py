# Generated by Django 4.2.1 on 2023-06-17 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=255)),
                ('Prenoms', models.CharField(max_length=255)),
                ('Diplomes', models.TextField()),
                ('Classes', models.CharField(blank=True, max_length=255)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='Prof')),
            ],
        ),
    ]
