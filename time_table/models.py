from django.db import models

from authentication.models import UserInfo
from master_forms.models import Course, Semester, Section, Subject, Lecture, Day, Time


class TimeTableMaster(models.Model):
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_sections = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.from_date) + '-' + str(self.to_date)


class TimeTableDetail(models.Model):
    fk_timetable_master = models.ForeignKey(TimeTableMaster, blank=True, null=True, on_delete=models.CASCADE)
    fk_subjects = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)
    fk_day = models.ForeignKey(Day, blank=True, null=True, on_delete=models.CASCADE)
    fk_lecture = models.ForeignKey(Lecture, blank=True, null=True, on_delete=models.CASCADE)
    fk_time_start = models.ForeignKey(Time, null=True, blank=True, related_name='fk_time_start',on_delete=models.CASCADE)
    fk_time_end = models.ForeignKey(Time, null=True, blank=True, related_name='fk_time_end', on_delete=models.CASCADE)
    lecture_break = models.CharField(max_length=20, blank=True, null=True)
    fk_faculty_user_info1 = models.ForeignKey(UserInfo, null=True, blank=True, related_name='fk_faculty_user_info1',on_delete=models.CASCADE)
    fk_faculty_user_info2 = models.ForeignKey(UserInfo, null=True, blank=True, related_name='fk_faculty_user_info2',on_delete=models.CASCADE)

    def __str__(self):
        return self.lecture_break
