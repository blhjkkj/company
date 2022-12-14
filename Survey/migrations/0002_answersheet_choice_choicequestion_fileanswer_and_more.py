# Generated by Django 4.0.6 on 2022-07-08 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='说明')),
                ('multi_choice', models.BooleanField(default=False, verbose_name='是否为多选')),
                ('order_in_list', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='问题')),
                ('required', models.BooleanField(default=True, help_text='这个问题是否必须回答')),
                ('order_in_list', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('multi_choice', models.BooleanField(default=False, verbose_name='是否为多选')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='uplod/questions')),
                ('is_image', models.BooleanField(default=True)),
                ('answer_sheet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Survey.answersheet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultiChoiceAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_sheet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Survey.answersheet')),
                ('choices', models.ManyToManyField(related_name='multi_choice_answers', to='Survey.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='multi_choice_answers', to='Survey.choicequestion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NonChoiceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='问题')),
                ('required', models.BooleanField(default=True, help_text='这个问题是否必须回答')),
                ('order_in_list', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.SmallIntegerField(choices=[(0, '问答题'), (1, '上传文件')], default=0, verbose_name='主观题类型')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建人')),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '调查问卷',
                'verbose_name_plural': '调查问卷',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SingleChoiceAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_sheet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Survey.answersheet')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='single_choice_answers', to='Survey.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='single_choice_answer_set', to='Survey.choicequestion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('answer_sheet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Survey.answersheet')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Survey.nonchoicequestion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='QAmodel',
        ),
        migrations.AddField(
            model_name='nonchoicequestion',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Survey.questionnaire'),
        ),
        migrations.AddField(
            model_name='fileanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Survey.nonchoicequestion'),
        ),
        migrations.AddField(
            model_name='choicequestion',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Survey.questionnaire'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='Survey.choicequestion'),
        ),
        migrations.AddField(
            model_name='answersheet',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Survey.questionnaire'),
        ),
        migrations.AddField(
            model_name='answersheet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='填表人'),
        ),
    ]
