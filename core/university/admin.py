from django.contrib import admin
from .models import University, Gallery


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass
# Register your models here.
