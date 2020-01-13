from django.db import models
from master_forms.models import Section, Semester, Course
from authentication.models import UserInfo


class StudentEvent(models.Model):
    """
    Student Event Database
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    event_details = models.CharField(max_length=500, blank=True, null=True)
    event_type = models.CharField(max_length=50, blank=True, null=True)
    event_form = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.event_title


class EventActivity(models.Model):
    """
    Event's activity database
    """
    fk_student_events = models.ForeignKey(StudentEvent, blank=True, null=True, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=50, blank=True, null=True)
    schedule_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    activity_details = models.CharField(max_length=500, blank=True, null=True)
    activity_type = models.CharField(max_length=10, blank=True, null=True)
    activity_venue = models.CharField(max_length=200, blank=True, null=True)
    propose = models.IntegerField(blank=True, null=True)
    allotted = models.IntegerField(blank=True, null=True)
    actual = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.activity_name


class EventMember(models.Model):
    """
    Event's members database
    """
    fk_student_events = models.ForeignKey(StudentEvent, blank=True, null=True, on_delete=models.CASCADE)
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_sections = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)


class ActivityMember(models.Model):
    """
    Activity members database
    """
    fk_event_member = models.ForeignKey(EventMember, blank=True, null=True, on_delete=models.CASCADE)
    fk_activity = models.ForeignKey(EventActivity, blank=True, null=True, on_delete=models.CASCADE)
    roles = models.CharField(max_length=30, blank=True, null=True)
    task = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.roles


class ActivityGuest(models.Model):
    """
    Activity guest database
    """
    fk_activity = models.ForeignKey(EventActivity, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    college = models.CharField(max_length=50, blank=True, null=True)
    purpose = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class ActivityItem(models.Model):
    """
    Activity's items database
    """
    fk_activity = models.ForeignKey(EventActivity, blank=True, null=True, on_delete=models.CASCADE)
    item = models.CharField(max_length=30, blank=True, null=True)
    item_cost = models.IntegerField(blank=True, null=True)
    item_quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.item


class EventRegistration(models.Model):
    """
    Database of students register for events
    """
    fk_student_events = models.ForeignKey(StudentEvent, blank=True, null=True, on_delete=models.CASCADE)
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    college = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    course_year = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.first_name + self.last_name


class ActivityGroupMember(models.Model):
    """
    Database of group member register for events
    """
    fk_events_registrations = models.ForeignKey(EventRegistration, blank=True, null=True, on_delete=models.CASCADE)
    fk_activity = models.ForeignKey(EventActivity, blank=True, null=True, on_delete=models.CASCADE)
    grp_member_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.grp_member_name
