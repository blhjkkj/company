# Generated by Django 4.0.6 on 2022-09-03 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_alter_comment_options_comment_xinw_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_date'], 'verbose_name': '评论管理', 'verbose_name_plural': '评论管理'},
        ),
    ]
