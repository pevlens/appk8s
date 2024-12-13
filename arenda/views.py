from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from .models import Category
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')  # Перенаправление на главную после регистрации

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # Автоматический вход после регистрации
        return response

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CategoryListView(TemplateView):
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Главные категории (без родителя)
        context['main_categories'] = Category.objects.filter(parent=None)
        return context

class SubcategoryListView(ListView):
    def get(self, request, *args, **kwargs):
        parent_id = self.kwargs.get('parent_id')
        try:
            parent_category = Category.objects.get(id=parent_id)
            subcategories = parent_category.children.all()
            data = {
                'subcategories': [
                    {'id': sub.id, 'name': sub.name} for sub in subcategories
                ]
            }
            return JsonResponse(data)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Parent category not found'}, status=404)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'