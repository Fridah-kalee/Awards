# Generated by Django 4.0.5 on 2022-06-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]
