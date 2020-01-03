from django.contrib import admin

from master_forms.models import AcademicSession, Module, Screen, UserType, UserRole, YearOfAdmission, UserOperation, \
    Nationality, State, City, District, Tehsil, PostalCode, Religion, Gender, BloodGroup, Course, Semester, Section, \
    TwelvethOrDiploma, StreamOrField, Subject, Day, Time, Lecture, Category, Reserved, ApplyingConcession, Cast, \
    SubCast, Degree, DegreeStreamOrField, PhysicallyChallenged, MotherTongue


class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'id')


admin.site.register(AcademicSession, AcademicSessionAdmin)


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'module_name')


admin.site.register(Module, ModuleAdmin)


class ScreenAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_module', 'screen_name')


admin.site.register(Screen, ScreenAdmin)


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_type')


admin.site.register(UserType, UserTypeAdmin)


class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_role')


admin.site.register(UserRole, UserRoleAdmin)


class YearOfAdmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'year_of_admission')


admin.site.register(YearOfAdmission, YearOfAdmissionAdmin)


class UserOperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_screen', 'fk_module', 'fk_user_role', 'status')


admin.site.register(UserOperation, UserOperationAdmin)


class NationalityAdmin(admin.ModelAdmin):
    list_display = ('nationality', 'id')


admin.site.register(Nationality, NationalityAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('state', 'id')


admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'id')


admin.site.register(City, CityAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'district')


admin.site.register(District, DistrictAdmin)


class TehsilAdmin(admin.ModelAdmin):
    list_display = ('id', 'tehsil')


admin.site.register(Tehsil, TehsilAdmin)


class PostalCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'postal_code')


admin.site.register(PostalCode, PostalCodeAdmin)


class MotherTongueAdmin(admin.ModelAdmin):
    list_display = ('mother_tongue', 'id')


admin.site.register(MotherTongue, MotherTongueAdmin)


class ReligionAdmin(admin.ModelAdmin):
    list_display = ('religion', 'id')


admin.site.register(Religion, ReligionAdmin)


class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender', 'id')


admin.site.register(Gender, GenderAdmin)


class BloodGroupAdmin(admin.ModelAdmin):
    list_display = ('blood_group', 'id')


admin.site.register(BloodGroup, BloodGroupAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'id')


admin.site.register(Course, CourseAdmin)


class SemesterAdmin(admin.ModelAdmin):
    list_display = ('semester', 'id')


admin.site.register(Semester, SemesterAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('sections', 'id')


admin.site.register(Section, SectionAdmin)


class TwelvethOrDiplomaAdmin(admin.ModelAdmin):
    list_display = ('twelveth_or_diploma', 'id')


admin.site.register(TwelvethOrDiploma, TwelvethOrDiplomaAdmin)


class StreamOrFieldAdmin(admin.ModelAdmin):
    list_display = ('stream_or_field_name', 'id')


admin.site.register(StreamOrField, StreamOrFieldAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subjects', 'id')


admin.site.register(Subject, SubjectAdmin)


class DayAdmin(admin.ModelAdmin):
    list_display = ('day', 'id')


admin.site.register(Day, DayAdmin)


class TimeAdmin(admin.ModelAdmin):
    list_display = ('time', 'id')


admin.site.register(Time, TimeAdmin)


class LectureAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'id')


admin.site.register(Lecture, LectureAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


admin.site.register(Category, CategoryAdmin)


class ReservedAdmin(admin.ModelAdmin):
    list_display = ('id', 'reserved')


admin.site.register(Reserved, ReservedAdmin)


class ApplyingConcessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'applying_concession')


admin.site.register(ApplyingConcession, ApplyingConcessionAdmin)


class CastAdmin(admin.ModelAdmin):
    list_display = ('id', 'cast')


admin.site.register(Cast, CastAdmin)


class SubCastAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_cast')


admin.site.register(SubCast, SubCastAdmin)


class DegreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'degree')


admin.site.register(Degree, DegreeAdmin)


class DegreeStreamOrFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'stream_or_field_name')


admin.site.register(DegreeStreamOrField, DegreeStreamOrFieldAdmin)


class PhysicallyChallengedAdmin(admin.ModelAdmin):
    list_display = ('id', 'physically_challenged')


admin.site.register(PhysicallyChallenged, PhysicallyChallengedAdmin)
