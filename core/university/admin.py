from django.contrib import admin
from .models import University, Degree, Faculty, FinanceAid, FAQ,  Gallery


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    pass


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass


@admin.register(FinanceAid)
class FinanceAidAdmin(admin.ModelAdmin):
    pass


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass
