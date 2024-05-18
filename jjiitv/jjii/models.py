from turtle import update
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Slider(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام اثر")
    poster = models.ImageField(null=True,blank=True,upload_to='images/', verbose_name='تصویر')
    des = models.TextField(max_length=400,verbose_name='توضیحات', null=True, blank=True)
    first = models.BooleanField(verbose_name="اولین اسلاید", null=True, blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.CharField(max_length=50, verbose_name="نام")
    subject = models.CharField(max_length=100, verbose_name="موضوع")
    message = models.TextField(max_length = 400, verbose_name = "پیام" )
    time = models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return self.subject


class Content(models.Model):
    type = models.CharField(max_length=60, verbose_name='نوع محتوا', blank=True, null=True)
    name = models.CharField(max_length=60, verbose_name='نام اثر', blank=True, null=True)
    story = stars= models.TextField(max_length=600, verbose_name='خلاصه داستان', blank=True, null=True)
    genre = models.CharField(max_length=100, verbose_name='ژانر', blank=True, null=True)
    country = models.CharField(max_length=60, verbose_name='کشور سازنده', blank=True, null=True)
    producer = models.CharField(max_length=60, verbose_name='تهیه کننده', blank=True, null=True)
    director = models.CharField(max_length=60, verbose_name='کارگردان', blank=True, null=True)
    writer = models.CharField(max_length=60, verbose_name='نویسنده', blank=True, null=True)
    stars= models.TextField(max_length=300, verbose_name='بازیگران', blank=True, null=True)
    language= models.TextField(max_length=300, verbose_name='زبان', blank=True, null=True)
    imdblink = models.CharField(max_length=200, verbose_name='پیوند آی ام دی بی', blank=True, null=True)
    imdbscore = models.CharField(max_length=200, verbose_name='امتیاز آی ام دی بی', blank=True, null=True)
    host= models.TextField(max_length=300, verbose_name='مجریان', blank=True, null=True)
    date = models.IntegerField(verbose_name='سال تولید', blank=True, null=True)
    episode = models.IntegerField(verbose_name='شماره اپیزود', blank=True, null=True)
    audience_age = models.IntegerField(verbose_name='حد پایین سن مخاطب', blank=True, null=True)
    view = models.IntegerField(verbose_name='دفعات پخش', default='1', blank=True, null=True)
    temp = models.IntegerField(verbose_name='دما', default='1', blank=True, null=True)
    score = models.IntegerField(verbose_name='امتیاز', default='1', blank=True, null=True)
    likes = models.IntegerField(verbose_name='لایک', default='0', blank=True, null=True)
    dislike = models.IntegerField(verbose_name='دیسلایک', default='0', blank=True, null=True)
    org = models.CharField(max_length=80, verbose_name='شبکه یا سازمان تولید کننده', blank=True, null=True)
    duration= models.IntegerField(verbose_name='مدت', default='0', blank=True, null=True)
    firstpage = models.BooleanField(verbose_name="اولین تصویر در اسلایدر باشد؟", null=True, blank=True)
    firstpagepriority = models.IntegerField(verbose_name=' اولویت نمایش صفحه ی اول در میان محتوای هم رده', default='0', blank=True, null=True)
    contentlink = models.TextField(max_length=400, verbose_name="پیوند محتوا بر روی سرور", blank=True, null=True )
    poster = models.ImageField(null=True,blank=True,upload_to='images/', verbose_name='تصویر اسلایدر')
    poster = models.ImageField(null=True,blank=True,upload_to='images/', verbose_name='تصویر کوچک')
    active = models.BooleanField(verbose_name="فعال", default=False, null=True, blank=True)


    def __str__(self):
        return self.name
    



    
    



