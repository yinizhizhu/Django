"""the models of the tutor system"""
from django.db import models

class content_student(models.Model):    #Done
    """this is for each student"""
    school = models.CharField(max_length = 15)
    grade = models.CharField(max_length = 15)
    wenli = models.BooleanField(default = True)
    subjects = models.CommaSeparatedIntegerField(max_length = 18)
    freestate = models.BooleanField(default = False)  #to judge the free state
    publishdate = models.DateTimeField(auto_now = True)
    timerequest = models.CommaSeparatedIntegerField(max_length = 42)
    sexrequest = models.IntegerField()
    judge = models.CharField(max_length = 50)
    costperhour = models.IntegerField()
    star = models.IntegerField(default = 0)
    evaluation = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.publishdate

class content_teacher(models.Model):    #Done
    wenli = models.BooleanField(default = True)
    subjects = models.CommaSeparatedIntegerField(max_length = 18)
    freestate = models.BooleanField(default = False)
    publishdate = models.DateTimeField(auto_now = True)
    timeforteaching = models.CommaSeparatedIntegerField(max_length = 42)
    getperhour = models.IntegerField()
    content_stu = models.ManyToManyField(content_student)
    def __unicode__(self):
        return self.publishdate

class Student(models.Model):    #Done
    """This is for the student"""
    name = models.CharField(max_length = 10)
    sex = models.BooleanField(default = True)
    age = models.IntegerField()
    tel = models.CharField(max_length = 15)
    email = models.EmailField()
    address = models.CharField(max_length = 50)
    content = models.ManyToManyField(content_student)
    def __unicode__(self):
        return self.name

class Teacher(models.Model):    #Done
    """This is for the teacher"""
    name = models.CharField(max_length = 10)
    sex = models.BooleanField(default=True)
    age = models.IntegerField()
    college = models.CharField(max_length = 20)
    major = models.CharField(max_length = 20)
    tel = models.CharField(max_length = 15)
    email = models.EmailField()
    address = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'photos')
    content = models.ManyToManyField(content_teacher)
    def __unicode__(self):
        return self.name

class User(models.Model):   #Done
    username = models.CharField(primary_key=True, max_length = 10)
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    teacher = models.ForeignKey(Teacher)
    student = models.ManyToManyField(Student) #the student of user
    def __unicode__(self):
        return self.username