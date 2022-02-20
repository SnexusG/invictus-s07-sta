from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, default='default_user', unique=True)
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=150, blank = True)
    gender_choices = (('M','male'),('F','female'),('-', 'rather not says'))
    gender = models.CharField(max_length=20, choices=gender_choices, default='-')
    email = models.EmailField(max_length=200, default = "new_user@gmail.com")
    password = models.CharField(max_length=200, default = "12345678")
    isExpert = models.BooleanField(default = False)
    isVerified = models.BooleanField(default = False)
    speciality = models.CharField(max_length=150, blank=True)
    documents_link = models.CharField(max_length = 200, blank = True)

    def save(self, *args, **kwargs):
        # self.country = self.country.lower()
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class Post(models.Model):
    authorID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default = 0)
    title = models.CharField(max_length = 100)
    body = models.TextField(blank = True)
    datePosted = models.DateTimeField(auto_now_add=True)
    stayAnonymous = models.BooleanField(default=False)

    class Meta:
        ordering = ['-datePosted']

    def __str__(self):
        return self.title

class Comment(models.Model):
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    authorID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default = 0)
    body = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datePosted', '-likes']



# invictushackathon 
# invictushackathongood