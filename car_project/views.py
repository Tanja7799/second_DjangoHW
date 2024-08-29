

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Car, Profile, Comment
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CommentForm, CarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



class CarListView(ListView):
    model = Car
    template_name = 'car_project/car/car_list.html'
    context_object_name = 'cars'
    paginate_by = 5
    ordering = ['id']

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_project/car/car_detail.html'
    context_object_name = 'car'


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


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_project/car/car_form.html'
    form_class = CarForm

    def form_valid(self, form):
        form.instance.user = self.request.user  #привязка користувача до пропозиції
        return super().form_valid(form)


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_project/car/car_form.html'
    fields = ['make', 'model', 'slug', 'country', 'body', 'power', 'fuel_type', 'is_available']

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_project/car/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')