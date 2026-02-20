from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .forms import CustomUserCreationForm
from .email_service import EmailService

import logging
logger = logging.getLogger(__name__)


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            EmailService.send_welcome_email(user)
            messages.success(request, "Registration successful! Welcome aboard.")
            login(request, user)
            return redirect('product_list')
        messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('product_list')

    if request.method == 'POST':
        email = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            EmailService.send_login_notification(user)
            messages.success(request, f"Welcome back, {user.first_name or user.email}!")
            next_url = request.GET.get('next', None)
            if next_url:
                return redirect(next_url)
            # Role-based redirect
            if user.role in ['admin', 'seller'] or user.is_superuser:
                return redirect('/admin/')
            return redirect('product_list')
        else:
            messages.error(request, "Invalid email or password. Please try again.")

    return render(request, 'registration/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        EmailService.send_logout_notification(request.user)
        logout(request)
        messages.success(request, "You have been logged out successfully.")
    return redirect('product_list')


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


@login_required
def delete_account_view(request):
    if request.method == 'POST':
        confirm = request.POST.get('confirm_delete', '')
        if confirm == 'DELETE':
            user = request.user
            email = user.email
            logout(request)
            user.delete()
            logger.info(f"Account deleted: {email}")
            messages.success(request, "Your account has been permanently deleted.")
            return redirect('product_list')
        else:
            messages.error(request, "Please type DELETE to confirm account deletion.")
    return render(request, 'accounts/delete_account.html')
