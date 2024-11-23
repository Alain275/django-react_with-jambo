from django.urls import path
from .views import hero_world_view

urlpatterns = [
    path('', hero_world_view, name='index'),
]
