from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Response(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional classes

    STUDENT_LEVEL = [('ug','Undergraduate'),('pgm','Postgraduate masters'), ('pgr','Postgraduate research')]
    student = models.CharField(max_length=20, choices=STUDENT_LEVEL, default=None, blank=True)

    PROFESSIONAL_LEVEL = [('low','(0 - 2)'),('moderate','(3 - 5)'), ('high','(5 - 10)'), ('advanced','(above 10)')]
    professional = models.CharField(max_length=20, choices=PROFESSIONAL_LEVEL, default=None, blank=True)

    creativity_meaning = models.TextField(max_length=2000, null=True)

    CREATIVE_PERSON = [('yes','Yes'),('no','No'),]
    creative = models.CharField(max_length=20, choices=CREATIVE_PERSON, default=None, blank=False)

    creativity_example = models.TextField(max_length = 2000, null=True)

    CHOICE_HAND = [('right','Right hand'),('left','Left hand'), ('both','Both hands')]
    hand = models.CharField(max_length=11, choices=CHOICE_HAND, default=None, blank=False)

    trial_signup = models.BooleanField(default=None, blank=True)

    def __str__(self):
        return self.user.username
