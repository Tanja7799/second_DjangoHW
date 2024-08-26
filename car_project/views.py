

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Car, Profile, Comment
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CommentForm


def car_list(request):
    cars = Car.objects.all().order_by('id')
    paginator = Paginator(cars, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'car_project/car/car_list.html', {'cars': page, 'page': page})


def car_detail(request, slug):
    car = get_object_or_404(Car, slug=slug)
    return render(request, 'car_project/car/car_detail.html', {'car': car})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Створено акаунт {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) ##instance=request.user візьмуться поточні дані з профілю
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context=context)

def logout_confirm(request):
    return render(request, 'users/logout_confirm.html')


@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comment_list')  # Перенаправляє на список коментарів
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})


def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')  # Отримання всіх коментарів, відсортованих за датою
    return render(request, 'comment_list.html', {'comments': comments})
