# Generated by Django 4.0.6 on 2022-07-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_delete_sptt_fist_remove_brand_addtime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='cont',
            field=models.IntegerField(blank=True, null=True, verbose_name='联系电话'),
        ),
    ]
