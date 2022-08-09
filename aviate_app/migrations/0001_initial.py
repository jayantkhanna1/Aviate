# Generated by Django 4.1 on 2022-08-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=100)),
                ('jobid', models.CharField(max_length=100)),
                ('name_of_applicant', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('resume', models.CharField(max_length=100)),
                ('cover_letter', models.CharField(max_length=100)),
                ('applicant_city', models.CharField(max_length=100)),
                ('applicant_state', models.CharField(max_length=100)),
                ('applicant_country', models.CharField(max_length=100)),
                ('candidate_image', models.CharField(max_length=100)),
                ('last_education', models.CharField(max_length=100)),
                ('last_edu_time', models.CharField(max_length=100)),
                ('last_edu_course', models.CharField(max_length=100)),
                ('last_edu_institute', models.CharField(max_length=100)),
                ('last_edu_percentage', models.CharField(max_length=100)),
                ('applicant_experience', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('city', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('Qualificaiton', models.CharField(max_length=100)),
                ('fromdate', models.CharField(max_length=100)),
                ('todate', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
