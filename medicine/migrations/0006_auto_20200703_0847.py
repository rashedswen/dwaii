# Generated by Django 2.2.7 on 2020-07-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0005_auto_20200630_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='img',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to='medicine/'),
        ),
    ]
