from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    '''
    Profile model that links with User to update it
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,null = True)
    first_name = models.CharField(max_length=30, blank=True)
    second_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/',null=True)
    contact = models.EmailField(max_length=100, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def delete_profile(self):
        self.delete()

    def __str__(self):
        return f'{self.user.username}'

class Post(models.Model):
    '''
    class that defines an instance of Image
    '''
    image = models.ImageField(upload_to='images/',null=True)
    title = models.CharField(max_length =30)
    location = models.CharField(max_length =30,null=True)
    description = models.CharField(max_length=100)
    url = models.URLField(max_length=255)
    profile = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering =['name']
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod 
    def all_posts(cls):
        return cls.objects.all()

    @classmethod
    def get_user_posts(cls,user):
        return cls.objects.filter(user=user)

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    def __str__(self):
        return self.title

class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.post} Rating'