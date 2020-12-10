from django.db import models


class University(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


class Gallery(models.Model):
    image = models.ImageField(upload_to='university_img')
    university = models.ForeignKey('University', on_delete=models.CASCADE, related_name='images')

