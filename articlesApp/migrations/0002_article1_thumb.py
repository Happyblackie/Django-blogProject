# Generated by Django 4.1.4 on 2022-12-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articlesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article1',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]