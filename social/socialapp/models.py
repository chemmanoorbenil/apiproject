from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=200)



    def __init__(self):
        return self.username



class Profile(models.Model):
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_img=models.ImageField
    about_me=models.CharField(max_length=200)
    cover_img=models.ImageField


    def __init__(self):
        return self.name
