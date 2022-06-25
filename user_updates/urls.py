from django.urls import path, include

urlpatterns = [
    path('', views.user_updates, name='user_updates')
]