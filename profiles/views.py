from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Diary
from .forms import UserProfileForm, DiaryForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def add_diary(request):
    """
    A view to allow the user to add a Diary entry
    """

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DiaryForm(request.POST)
            if form.is_valid():
                diary = form.save(commit=False)
                diary.user = request.user
                diary.save()
                messages.success(request, 'Your review was successful')
                return render(request, 'profiles/profile.html')
            else:
                messages.error(
                    request, 'Failed to add your review')
    context = {
        'form': form
    }

    return render(request, context)


@login_required
def edit_diary(request, diary_id):
    """
    A view to allow the users to edit their own review
    """

    diary = get_object_or_404(Diary, pk=diary_id)

    if request.method == 'POST':
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            messages.info(request, 'Review has been changed')
            return render(request, 'profiles/profile.html')
        else:
            messages.error(
                request, 'Review edit failed, Please try again')

    else:
        form = DiaryForm(instance=diary)

    messages.info(request, 'You are editing your review')
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'diary': diary,
        'edit': True,
    }
    return render(request, template, context)