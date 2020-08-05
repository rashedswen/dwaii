# Generated by Django 3.0.7 on 2020-08-01 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_auto_20200801_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='medCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='medType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='medicine',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medType'),
        ),
    ]
