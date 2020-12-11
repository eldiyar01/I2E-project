from django.db import models
from django.urls import reverse


class University(models.Model):
    title = models.CharField(max_length=200)
    headnote = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('university:details', kwargs={'pk': self.pk})


class Gallery(models.Model):
    image = models.ImageField(upload_to='university_img')
    university = models.ForeignKey('University', on_delete=models.CASCADE, related_name='images')

