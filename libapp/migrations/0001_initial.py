# Generated by Django 5.0.6 on 2024-07-10 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Address', models.CharField(blank=True, max_length=50, null=True)),
                ('Course', models.CharField(blank=True, max_length=50, null=True)),
                ('Gender', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
