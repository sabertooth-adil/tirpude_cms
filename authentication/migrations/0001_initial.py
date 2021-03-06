# Generated by Django 3.0.1 on 2020-01-15 08:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master_forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, default='Inactive', max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, max_length=30, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_no2', models.CharField(blank=True, max_length=20, null=True)),
                ('aadhar_no', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('registration_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('fk_blood_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.BloodGroup')),
                ('fk_gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.Gender')),
                ('fk_mother_tongue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.MotherTongue')),
                ('fk_nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.Nationality')),
                ('fk_religion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.Religion')),
                ('fk_user_role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.UserRole')),
                ('fk_user_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.UserType')),
            ],
        ),
        migrations.CreateModel(
            name='AddressDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200)),
                ('tehsil', models.CharField(blank=True, max_length=100)),
                ('pin_code', models.CharField(blank=True, max_length=20)),
                ('correspondence_address', models.CharField(blank=True, max_length=200, null=True)),
                ('correspondence_tehsil', models.CharField(blank=True, max_length=100)),
                ('correspondence_pin_code', models.CharField(blank=True, max_length=20, null=True)),
                ('fk_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_city', to='master_forms.City')),
                ('fk_correspondence_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_correspondence_city', to='master_forms.City')),
                ('fk_correspondence_district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_correspondence_district', to='master_forms.District')),
                ('fk_correspondence_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_correspondence_state', to='master_forms.State')),
                ('fk_district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_district', to='master_forms.District')),
                ('fk_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_state', to='master_forms.State')),
                ('fk_user_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField(blank=True, null=True)),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('school_board', models.CharField(blank=True, max_length=30, null=True)),
                ('school_place', models.CharField(blank=True, max_length=30, null=True)),
                ('tenth_year_of_passing', models.DateField(blank=True, max_length=30, null=True)),
                ('tenth_marks', models.IntegerField(blank=True, null=True)),
                ('tenth_out_of', models.IntegerField(blank=True, null=True)),
                ('school_percentage', models.CharField(blank=True, max_length=10, null=True)),
                ('college_name', models.CharField(blank=True, max_length=100, null=True)),
                ('college_board_or_university', models.CharField(blank=True, max_length=30, null=True)),
                ('college_place', models.CharField(blank=True, max_length=30, null=True)),
                ('college_date_of_passing', models.DateField(blank=True, max_length=30, null=True)),
                ('college_total_marks', models.IntegerField(blank=True, null=True)),
                ('college_marks_out_of', models.IntegerField(blank=True, null=True)),
                ('college_percentage', models.CharField(blank=True, max_length=30, null=True)),
                ('degree_college_name', models.CharField(blank=True, max_length=100, null=True)),
                ('degree_college_board_or_university', models.CharField(blank=True, max_length=100, null=True)),
                ('degree_college_place', models.CharField(blank=True, max_length=100, null=True)),
                ('degree_college_date_of_passing', models.DateField(blank=True, max_length=30, null=True)),
                ('degree_college_total_marks', models.IntegerField(blank=True, null=True)),
                ('degree_college_marks_out_of', models.IntegerField(blank=True, null=True)),
                ('degree_college_percentage', models.IntegerField(blank=True, null=True)),
                ('guardian_name', models.CharField(blank=True, max_length=30, null=True)),
                ('occupation_of_guardian', models.CharField(blank=True, max_length=30, null=True)),
                ('annual_income_of_guardian', models.CharField(blank=True, max_length=30, null=True)),
                ('relationship_with_guardian', models.CharField(blank=True, max_length=30, null=True)),
                ('guardian_mobile_no', models.CharField(blank=True, max_length=30, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('fk_academic_session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.AcademicSession')),
                ('fk_applying_concession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.ApplyingConcession')),
                ('fk_cast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.Cast')),
                ('fk_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.Category')),
                ('fk_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.Course')),
                ('fk_degree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.Degree')),
                ('fk_degree_stream_or_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.DegreeStreamOrField')),
                ('fk_domicile_of_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.State')),
                ('fk_physically_challenged', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.PhysicallyChallenged')),
                ('fk_reserved', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.Reserved')),
                ('fk_sections', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.Section')),
                ('fk_semesters', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.Semester')),
                ('fk_stream_or_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.StreamOrField')),
                ('fk_sub_cast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.SubCast')),
                ('fk_twelveth_or_diploma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.TwelvethOrDiploma')),
                ('fk_user_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.UserInfo')),
                ('fk_year_of_admission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master_forms.YearOfAdmission')),
            ],
        ),
    ]
