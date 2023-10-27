from django.db import models
#

class About(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    photo_head = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='default.jpg')
    photo_content = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='default.jpg')
    description = models.TextField(blank=True, null=True, default='Default Text')
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    social_media_accounts = models.JSONField(blank=True, null=True, default={"key": "value"})

