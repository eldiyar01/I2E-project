from django.urls import path
from .views import home, university_dtl, search_result

app_name = 'university'
urlpatterns = [
    path('', home, name='home'),
    path('details/<int:pk>', university_dtl, name='details'),
    path('search-result/', search_result, name='search-result'),

]
