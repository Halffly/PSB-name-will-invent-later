# Generated by Django 3.0.6 on 2021-04-17 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_file_date_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
