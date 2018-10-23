# Generated by Django 2.1.2 on 2018-10-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
