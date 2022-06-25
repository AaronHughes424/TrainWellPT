from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('add_diary/', views.add_diary, name='add_diary'),
    path('edit_diary/<int:diary_id>/', views.edit_diary, name='edit_diary'),
]