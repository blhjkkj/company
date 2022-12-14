# Generated by Django 4.0.6 on 2022-07-15 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0002_answersheet_choice_choicequestion_fileanswer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='choicequestion',
            name='questionnaire',
        ),
        migrations.RemoveField(
            model_name='fileanswer',
            name='answer_sheet',
        ),
        migrations.RemoveField(
            model_name='fileanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='multichoiceanswer',
            name='answer_sheet',
        ),
        migrations.RemoveField(
            model_name='multichoiceanswer',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='multichoiceanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='nonchoicequestion',
            name='questionnaire',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='user',
        ),
        migrations.RemoveField(
            model_name='singlechoiceanswer',
            name='answer_sheet',
        ),
        migrations.RemoveField(
            model_name='singlechoiceanswer',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='singlechoiceanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='textanswer',
            name='answer_sheet',
        ),
        migrations.RemoveField(
            model_name='textanswer',
            name='question',
        ),
        migrations.DeleteModel(
            name='AnswerSheet',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='ChoiceQuestion',
        ),
        migrations.DeleteModel(
            name='FileAnswer',
        ),
        migrations.DeleteModel(
            name='MultiChoiceAnswer',
        ),
        migrations.DeleteModel(
            name='NonChoiceQuestion',
        ),
        migrations.DeleteModel(
            name='Questionnaire',
        ),
        migrations.DeleteModel(
            name='SingleChoiceAnswer',
        ),
        migrations.DeleteModel(
            name='TextAnswer',
        ),
    ]
