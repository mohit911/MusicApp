"""Models Defenition."""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
GENDER_CHOICES = (('Others', 'Others'), ('Male', 'Male'), ('Female', 'Female'))


class UserProfileInfo(models.Model):
    """Class to store User Profile."""

    user = models.OneToOneField(
        User,
        blank=False,
        null=False)

    first_name = models.CharField(
        default='',
        max_length=255,
        blank=False,
        null=False)

    last_name = models.CharField(
        default='',
        max_length=255,
        blank=False,
        null=False)

    gender = models.CharField(
        max_length=8,
        choices=GENDER_CHOICES)

    profile_picture = models.ImageField(upload_to='User/Profile Picture')

    joining_date = models.DateTimeField(
        default=timezone.now)

    def __unicode__(self):
        """Unicode method to display Username in Admin."""
        return str(self.user.username)

    class Meta:
        """Information About the class."""

        verbose_name = "UserProfileInfo"
        verbose_name_plural = "UserProfileInfo"
