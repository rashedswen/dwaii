# Generated by Django 3.0.7 on 2020-06-24 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_auto_20200624_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='createDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
