from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_updates, name='uesr_updates'),
    # path('add_diary/', views.add_diary, name='add_diary'),
]