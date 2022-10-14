from django.contrib.auth import get_user_model
from django.db import models

# UserModel = get_user_model()


class UserModel(models.Model):
    user_type = models.BooleanField()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class MentorsModel(models.Model):
    fist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    web_site = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    user_id = models.OneToOneField(UserModel, on_delete=models.RESTRICT, related_name='user1',)

    def __str__(self):
        return self.fist_name

    class Meta:
        verbose_name = 'mentor'
        verbose_name_plural = 'mentors'


class CourseModel(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=250)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class GroupsModel(models.Model):
    group_name = models.CharField(max_length=100)
    mentor_id = models.ForeignKey(MentorsModel, on_delete=models.RESTRICT, related_name='mentor_id')
    course_id = models.ForeignKey(CourseModel, on_delete=models.RESTRICT, related_name='course_id')

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'


class StudentsModel(models.Model):
    fist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    id_card = models.CharField(max_length=100)
    group_id = models.ForeignKey(GroupsModel, on_delete=models.RESTRICT, related_name='group')
    user_id = models.OneToOneField(UserModel, on_delete=models.RESTRICT, related_name='user2')

    def __str__(self):
        return self.fist_name

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'