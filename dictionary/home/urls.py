from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('word',views.word,name='word')
]