from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

# Create your models here.
GENDER__CHOICES = [
    ("Male","Male"),
    ("Female","Female"),
]

SPESIFICATION__CHOICES = [
    ("Frontend","Frontend"),
    ("Backend","Backend"),
    ("Ingliz tili","Ingliz tili"),
    ("Rus tili","Rus tili"),
    ("Xitoy tili","Xitoy tili"),
    ("Matematika","Matematika"),
    ("Mental Arifmetika","Mental Arifmetika"),
    ("Mobile/Android","Mobile/Android"),
    ("Mobile/Ios","Mobile/Ios"),
    ("Mobile/Flutter","Mobile/Flutter"),
]

ROOM__CHOICES = [
    ("Room-1","Room-1"),
    ("Room-2","Room-2"),
    ("Room-3","Room-3"),
    ("Room-4","Room-4"),
    ("Room-5","Room-5"),
    ("Room-Extra","Room-Extra"),
]

TIME__CHOICES = [
    ("10:00 - 12:00","10:00 - 12:00"),
    ("14:00 - 16:00","14:00 - 16:00"),
    ("16:00 - 18:00","16:00 - 18:00"),
    ("18:00 - 20:00","18:00 - 20:00"),
    ]






class Mentor(models.Model):
    full_name = models.CharField(max_length=100)
    spesification = models.CharField(max_length=20,choices=SPESIFICATION__CHOICES,default="Backend")
    gender = models.CharField(max_length=6,choices=GENDER__CHOICES,default="Male")
    birth_date = models.DateField()
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    adress = models.CharField(max_length=70) 
    image = models.ImageField(upload_to='mentor')
    salary = MoneyField(max_digits=3, decimal_places=0, default_currency='USD')


    def final_salary(self):
        one_per = self.salary / 100
        twelf_per = one_per * 12
        final_salary = self.salary - twelf_per
        return final_salary

    def __str__(self):
        return self.full_name


class Group(models.Model):
    title = models.CharField(max_length=30)
    spesification = models.CharField(max_length=20,choices=SPESIFICATION__CHOICES,default="Frontend")
    mentor = models.OneToOneField(Mentor,on_delete=models.SET_NULL,null=True)
    lesson_qty = models.IntegerField()
    student_qty = models.IntegerField()
    price = MoneyField(max_digits=3, decimal_places=0, default_currency='USD')
    time = models.CharField(max_length=14,choices=TIME__CHOICES,default="10:00 - 12:00")
    room  = models.CharField(max_length=11,choices=ROOM__CHOICES,default="Room-Extra")


    def total_incom(self):
        total_incom = self.price * self.student_qty
        return total_incom

    def salary(self):
        bir_foizi = self.total_incom / 100 
        qirq_foizi = bir_foizi * 40
        salary = self.total_incom - qirq_foizi
        return salary

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=70)
    gender = models.CharField(max_length=6,choices=GENDER__CHOICES,default="Male")
    spesification = models.CharField(max_length=20,choices=SPESIFICATION__CHOICES,default="Backend")
    city = models.CharField(max_length=50)
    adress = models.CharField(max_length=70)
    image = models.ImageField(upload_to='mentor')


    def __str__(self):
        return self.full_name


class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    address = models.CharField(max_length=60)
    spesification = models.CharField(max_length=20,choices=SPESIFICATION__CHOICES,default="Backend")
    gender = models.CharField(max_length=6,choices=GENDER__CHOICES,default="Male")
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='user_profile')
    about = models.TextField()

    def __str__(self):
        return self.username
