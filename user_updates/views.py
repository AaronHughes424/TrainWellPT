from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Diary
from .forms import DiaryForm

# Create your views here.


@login_required
def user_updates(request):
    """ A view to retunr the index page """

    return render(request, 'user_update/user_update.html')


# @login_required
# def add_update(request):
#     """
#     A view to allow the user to add a Diary entry
#     """

#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = DiaryForm(request.POST)
#             if form.is_valid():
#                 diary = form.save(commit=False)
#                 diary.user = request.user
#                 diary.save()
#                 messages.success(request, 'Your review was successful')
#                 return redirect(reverse('profile', args=[diary.id]))
#             else:
#                 messages.error(
#                     request, 'Failed to add your review')
#     context = {
#         'form': form
#     }

#     return render(request, context)


# @login_required
# def edit_update(request, diary_id):
#     """
#     A view to allow the users to edit their own review
#     """

#     diary = get_object_or_404(Diary, pk=diary_id)

#     if request.method == 'POST':
#         form = DiaryForm(request.POST, instance=diary)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Review has been changed')
#             return redirect(reverse('profile', args=[diary.id]))
#         else:
#             messages.error(
#                 request, 'Review edit failed, Please try again')

#     else:
#         form = DiaryForm(instance=diary)

#     messages.info(request, 'You are editing your review')
#     template = 'profiles/profile.html'
#     context = {
#         'form': form,
#         'diary': diary,
#         'edit': True,
#     }
#     return render(request, template, context)
