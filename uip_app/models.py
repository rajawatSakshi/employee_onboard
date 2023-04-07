from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=False,null = False)
    username = models.CharField(max_length=200, null = True,unique=True)
    employee_id = models.IntegerField(unique=True,null = False)
    email = models.CharField(max_length=200, blank=False,unique=True)
    role_id = models.IntegerField(blank=False, null=False, default=0)
    oragnization_id = models.IntegerField(blank=False, null=False, default=0)
    permissions_id = models.IntegerField(blank=False, null=False, default=0)
    department_id = models.IntegerField(blank=True,null=True, default=0)

    def __str__(self):
        return f"{self.username}"
    
class Department(models.Model):
    id = models.IntegerField(blank=False,primary_key=True)
    department_name = models.CharField(max_length=100, blank=True, default='')
    active = models.BooleanField(default=True)

class Role(models.Model):
    id = models.IntegerField(blank=False,primary_key=True)
    role = models.CharField(max_length=100, blank=True, default='')
    department_id = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

class Organisation(models.Model):
    id = models.IntegerField(blank=False,primary_key=True)
    organisation_name = models.CharField(max_length=100, blank=True, default='')
    user_id = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

class Questions(models.Model):
    id = models.IntegerField(blank=False,primary_key=True)
    question = models.CharField(max_length=100, blank=True, default='')
    department_id = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    Is_basic = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

class Answers(models.Model):
    id = models.IntegerField(blank=False,primary_key=True)
    Answers = models.CharField(max_length=1000, blank=True, default='')
    question_id = models.ForeignKey(Questions, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

class UsersAnswers(models.Model):
    id = models.IntegerField(blank=False,primary_key=True)
    Answers = models.CharField(max_length=1000, blank=True, default='')
    # question_id = models.IntegerField(null=False, blank=False)
    user_id = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)    

class Permissions(models.Model):
    id = models.IntegerField(blank=False,primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    user_id = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)   


class Notifications(models.Model):
    id = models.IntegerField(blank=False,primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    user_id = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)       

    class Meta:
        ordering = ['id']