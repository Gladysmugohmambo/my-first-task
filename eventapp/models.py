from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

def __str__(self):
  return self.user.username

class Profile(models.Model):
	uer = models.OneToOneField(User, on_delete=models.CASCADE)
	email_confirmed = models.BooleanField(default=False)
	bio = models.TextField(max_length=500, blank=True)
	location= models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
    	Profile.objects.create(user=instance)
    	instance.profile.save()

# Create your model




































