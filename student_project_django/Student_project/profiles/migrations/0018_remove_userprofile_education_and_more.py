# Generated by Django 5.0.6 on 2025-01-22 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_userprofile_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='university',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_company',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Current Company'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_company_position',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Current Position'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_company_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date at Current Company'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Current Salary'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='expected_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Expected Salary'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='preferred_location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Preferred Job Location'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='previous_company',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Previous Company'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='previous_company_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End Date at Previous Company'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='previous_company_position',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Previous Position'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='previous_company_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date at Previous Company'),
        ),
        migrations.CreateModel(
            name='EducationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(blank=True, max_length=255, null=True, verbose_name='Education Level')),
                ('degree', models.CharField(blank=True, max_length=255, null=True, verbose_name='Degree')),
                ('specialization', models.CharField(blank=True, max_length=255, null=True, verbose_name='Specialization/Stream')),
                ('college_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='College Name')),
                ('university', models.CharField(blank=True, max_length=255, null=True, verbose_name='University Name')),
                ('start_year', models.PositiveIntegerField(verbose_name='Start Year')),
                ('end_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='End Year')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='profiles.userprofile')),
            ],
        ),
    ]
