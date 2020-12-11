from django.db import models
from django.urls import reverse


class University(models.Model):
    title = models.CharField(max_length=200)
    headnote = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('university:details', kwargs={'pk': self.pk})


class Degree(models.Model):
    university = models.ForeignKey('University', on_delete=models.CASCADE, related_name='degrees')
    qualifications = models.CharField(max_length=50)
    information = models.TextField()


class Faculty(models.Model):
    degree = models.ForeignKey('Degree', on_delete=models.CASCADE, related_name='faculties')
    title = models.CharField(max_length=100)
    LANGUAGES_CHOICES = (('KG', 'Kyrgyz'), ('RU', 'Russian'), ('EN', 'English'), ('TU', 'Turkish'))
    language = models.CharField(max_length=2, choices=LANGUAGES_CHOICES, default='Russian')
    description = models.TextField()
    duration = models.IntegerField(default=4)
    fee = models.IntegerField()


class FinanceAid(models.Model):
    university = models.ForeignKey('University', on_delete=models.CASCADE, related_name='aid')
    title = models.CharField(max_length=100)
    description = models.TextField()


class FAQ(models.Model):
    university = models.ForeignKey('University', on_delete=models.CASCADE, related_name='faq')
    title = models.CharField(max_length=100, default='Frequently asked Question')
    description = models.TextField()


class Gallery(models.Model):
    university = models.ForeignKey('University', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='university_img')


