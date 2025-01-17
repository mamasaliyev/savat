# Generated by Django 5.1.2 on 2024-10-17 11:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savatcha', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savat',
            name='descr',
        ),
        migrations.RemoveField(
            model_name='savat',
            name='soni',
        ),
        migrations.RemoveField(
            model_name='savat',
            name='title',
        ),
        migrations.AddField(
            model_name='mahsulot',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='mahsulot',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mahsulot_images/'),
        ),
        migrations.AddField(
            model_name='mahsulot',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mahsulot',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='savat',
            name='miqdor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='price',
            field=models.IntegerField(),
        ),
    ]
