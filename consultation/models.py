# from django.db import models
# from django.contrib.auth.models import User

# class Schedule(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     day = models.CharField(max_length=10, choices=[
#         ('Monday', 'Monday'),
#         ('Tuesday', 'Tuesday'),
#         ('Wednesday', 'Wednesday'),
#         ('Thursday', 'Thursday'),
#         ('Friday', 'Friday'),
#         ('Saturday', 'Saturday'),
#         ('Sunday', 'Sunday'),
#     ])
#     time_period = models.CharField(max_length=100)

#     class Meta:
#         unique_together = ('user', 'name', 'day', 'time_period')

#     def __str__(self):
#         return f"{self.name} - {self.day} - {self.time_period}"
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=[
        ('Dr. Fardin','Dr. Fardin'),
        ('Dr. Mehedi','Dr. Mehedi'),
        ('Dr. Maliha','Dr. Maliha'),
        ('Dr. Isha','Dr. Isha'),
    ])
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Sunday', 'Sunday'),
    ])
    time_period = models.CharField(max_length=100, choices=[
        ('8:00am','8:00am'),
        ('9:00am','9:00am'),
        ('10:00am','10:00am'),
        ('11:00am','11:00am'),
        ('12:00pm','12:00pm'),
        ('1:00pm','1:00pm'),
    ])

    class Meta:
        unique_together = ('user', 'name', 'day', 'time_period')

    def __str__(self):
        return f"{self.name} - {self.day} - {self.time_period}"