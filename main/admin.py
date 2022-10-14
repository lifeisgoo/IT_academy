from django.contrib import admin
from .models import UserModel, MentorsModel, GroupsModel, StudentsModel, CourseModel

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_type']
    list_display_links = ['id', 'user_type']


@admin.register(MentorsModel)
class MentorsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'experience']
    list_display_links = ['id', 'first_name', 'experience']


@admin.register(GroupsModel)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_name', 'mentor_id']
    list_display_links = ['id', 'group_name', 'mentor_id']


@admin.register(StudentsModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'group_id']
    list_display_links = ['id', 'first_name', 'group_id']


@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'duration']
    list_display_links = ['id', 'course_name', 'duration']