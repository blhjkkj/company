# Generated by Django 4.0.6 on 2022-07-25 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_shangping_pic1_shangping_pic2_shangping_pic3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shangping',
            name='pic',
        ),
    ]
