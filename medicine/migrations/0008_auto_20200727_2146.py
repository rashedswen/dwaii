# Generated by Django 2.2.7 on 2020-07-27 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0007_auto_20200711_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='is_pharmacy',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='location',
        ),
        migrations.AddField(
            model_name='medicine',
            name='arabicName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='category',
            field=models.CharField(choices=[('', 'أدوية القلب والاوعية الدموية'), ('', 'ادوية الجهاز الهضمى'), ('', 'مكملات الغذاء والفيتامين'), ('', 'أدوية العدوى البكتيرية'), ('', 'أدوية جهاز المناعة'), ('', 'مأكولات و مشروبات'), ('', 'الجهاز العضلى العظمى'), ('', 'أدوية العين والأذن والأنف'), ('', 'المستحضرات الموضعية'), ('', 'ادوية الجهاز التنفسى'), ('', 'أدوية الجهاز العصبي'), ('', 'أدوية العدوى البكتيرية'), ('', 'ادوية الغدد الصماء'), ('', 'المسالك البولية والتناسلية'), ('', 'أدوية الكيماوي')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='manufactureCompanyAr',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='manufactureCompanyEn',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='type',
            field=models.CharField(choices=[('tablet', 'حبوب'), ('capsule', 'كبسولات'), ('syrup', 'شراب'), ('injection', 'حقن'), ('nasalDrops', 'قطرة أنف'), ('nasalSpray', 'بخاخ أنف'), ('eyeDrops', 'قطرة عين'), ('cream', 'كريم'), ('gel', 'جيل'), ('pen', 'قلم'), ('eyeOint', 'مرهم عين'), ('earDrops', 'قطرة أذن')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_info',
            name='accType',
            field=models.CharField(choices=[('no', 'عادي'), ('ph', 'صيدلية'), ('or', 'مبادرة'), ('ve', 'بائع')], default='no', max_length=3),
        ),
        migrations.AddField(
            model_name='user_info',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='pharmacyName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='requestMedi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicineGeneral', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, default='profile.png', null=True, upload_to='medicine/request/new/')),
                ('description', models.TextField(blank=True, null=True)),
                ('requestDate', models.DateTimeField(auto_now_add=True)),
                ('prescription', models.ImageField(blank=True, null=True, upload_to='medicine/request/')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
