from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def user_updates(request):
    """ A view to retunr the index page """

    return render(request, 'user_update/user_update.html')
