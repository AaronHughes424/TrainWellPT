from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Diary(models.Model):
#     """
#     Diary Model
#     """

#     class Meta:
#         ordering = ['-date_added']

#     user = models.ForeignKey(User,
#                              null=True,
#                              blank=True,
#                              on_delete=models.CASCADE)
#     title = models.CharField(max_length=254)
#     content = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title