# Generated by Django 4.0.3 on 2022-05-23 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=5000)),
                ('link', models.CharField(max_length=255)),
                ('date_published', models.DateTimeField(verbose_name='date published')),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
    ]
