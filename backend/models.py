from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.fields import FloatField


class UserManager(BaseUserManager):

    def create_user(self, username, name, surname, email, password, **other_fields):

        email = self.normalize_email(email)
        user = self.model(username=username, name=name,
                          surname=surname, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, name, surname, email, password, **other_fields):

        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, name, surname, email, password, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=25, unique=True, verbose_name="Username")
    name = models.CharField(
        max_length=25, verbose_name="Name")
    surname = models.CharField(
        max_length=25, verbose_name="Surname")
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_staff = models.BooleanField(default=False, verbose_name="Operator")
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'surname', 'email']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class Project(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Project")
    fullname = models.TextField(
        max_length=200, verbose_name="Full name of Project")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
class Room(models.Model):
    index = models.CharField(
        max_length=50, verbose_name="Room index")
    description = models.TextField(
        max_length=200, verbose_name="Room name")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Project")
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Responsible")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
    

class Quality_issue(models.Model):
    name = models.CharField(max_length=25, verbose_name="Issue")
    description = models.TextField(max_length=200,verbose_name="Description")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Quality issue"
        verbose_name_plural = "Quality issues"
    
class Safety_issue(models.Model):
    name = models.CharField(max_length=25, verbose_name="Issue")
    description = models.TextField(max_length=200,verbose_name="Description")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Safety issue"
        verbose_name_plural = "Safety issues"

class Report_Safety(models.Model):
    statuses = [('Active','Active'),('On going','On going'),('Solved','Solved'),('Waiting for approval','Waiting for approval')]
    photo = models.ImageField(upload_to="safety", verbose_name="Photo")
    name = models.CharField(
        max_length=50, verbose_name="Issue name")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author",related_name="safety_issue_author")
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Responsible",related_name="safety_issue_responsible")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Room")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(verbose_name="Last Updated")
    is_active = models.BooleanField(verbose_name="Activity")
    status = models.CharField(max_length=50, verbose_name="Status", choices=statuses, default="Active")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Safety report"
        verbose_name_plural = "Safety reports"
    
class Report_Quality(models.Model):
    statuses = [('Active','Active'),('On going','On going'),('Solved','Solved'),('Waiting for approval','Waiting for approval')]
    photo = models.ImageField(upload_to="quality", verbose_name="photo")
    issue = models.ForeignKey(Quality_issue, on_delete=models.CASCADE,verbose_name="Issue")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author",related_name="quality_issue_author")
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Responsible",related_name="quality_issue_responsible")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Room")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(verbose_name="Last Updated")
    is_active = models.BooleanField(verbose_name="Activity")
    status = models.CharField(max_length=50, verbose_name="Status", choices=statuses, default="Active")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Quality report"
        verbose_name_plural = "Quality reports"
    

