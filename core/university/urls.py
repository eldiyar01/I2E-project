from django.urls import path
from .views import home, university_dtl, fast_search, searcher, searcher_res, features, team

app_name = 'university'
urlpatterns = [
    path('', home, name='home'),
    path('details/<int:pk>', university_dtl, name='details'),
    path('fast-search/', fast_search, name='fast-search'),
    path('searcher/', searcher, name='searcher'),
    path('searcher-result/', searcher_res, name='searcher-res'),
    path('features/', features, name='features'),
    path('team', team, name='team'),
]
