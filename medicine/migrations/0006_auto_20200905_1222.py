# Generated by Django 3.1.1 on 2020-09-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0005_auto_20200904_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacyacc',
            name='licenseImg',
            field=models.ImageField(blank=True, null=True, upload_to='license/'),
        ),
        migrations.AlterField(
            model_name='pharmacyacc',
            name='licenseNumber',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.RemoveField(
            model_name='storage',
            name='medicine',
        ),
        migrations.AddField(
            model_name='storage',
            name='medicine',
            field=models.ManyToManyField(to='medicine.medicine'),
        ),
    ]