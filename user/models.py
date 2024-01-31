from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def profile(self):
        profile = Profile.objects.get(user=self)


# class Profile(models.Model):
#     class Meta:
#         verbose_name_plural = 'User Profiles'
#         verbose_name = 'User Profile'
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=1000, blank=True, null=True)
#     bio = models.CharField(max_length=100, blank=True, null=True)
#     image = models.ImageField(upload_to="user_images", default="default.jpg")
#     cv = models.FileField(blank=True, null=True, upload_to="cv")
#     verified = models.BooleanField(default=False)


# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# def __str__(self):
#     return f'{self.user.first_name} {self.user.last_name}'


# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)
