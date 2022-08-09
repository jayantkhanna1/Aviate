# Generated by Django 4.1 on 2022-08-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviate_app', '0003_rename_qualificaiton_jobs_qualification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='last_edu_course',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='last_edu_institute',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='last_edu_percentage',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='last_edu_time',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='last_education',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='candidate_exp',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='candidate_qual',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='dob',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
