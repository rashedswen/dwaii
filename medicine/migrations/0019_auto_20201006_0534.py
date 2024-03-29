# Generated by Django 2.2.7 on 2020-10-06 05:34

from django.db import migrations, models
import medicine.models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0018_auto_20200905_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='arabicName',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pharmacyacc',
            name='licenseImg',
            field=models.ImageField(upload_to=medicine.models.encodePath),
        ),
    ]
