from django.shortcuts import render

# Create your views here.

def user_updates(request):
    """ A view to retunr the index page """
    
    return render(request, 'user_updates/user_updates.html')