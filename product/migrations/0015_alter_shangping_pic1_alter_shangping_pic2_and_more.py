# Generated by Django 4.0.6 on 2022-07-29 03:49

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_shangping_pic1_alter_shangping_pic2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shangping',
            name='pic1',
            field=models.ImageField(default='', upload_to=product.models.get_upload_path, verbose_name='图片1'),
        ),
        migrations.AlterField(
            model_name='shangping',
            name='pic2',
            field=models.ImageField(default='', upload_to=product.models.get_upload_path, verbose_name='图片2'),
        ),
        migrations.AlterField(
            model_name='shangping',
            name='pic3',
            field=models.ImageField(default='', upload_to=product.models.get_upload_path, verbose_name='图片3'),
        ),
        migrations.AlterField(
            model_name='shangping',
            name='pic4',
            field=models.ImageField(default='', upload_to=product.models.get_upload_path, verbose_name='图片4'),
        ),
        migrations.AlterField(
            model_name='shangping',
            name='pic5',
            field=models.ImageField(default='', upload_to=product.models.get_upload_path, verbose_name='图片5'),
        ),
        migrations.AlterField(
            model_name='shangping',
            name='video',
            field=models.FileField(default='', upload_to=product.models.get_upload_path, verbose_name='产品视频'),
        ),
    ]
