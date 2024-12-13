from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from .views import *

urlpatterns = [
    # Ваши URL-шаблоны
    path('accounts/', include('django.contrib.auth.urls')),  # Встроенные URL для аутентификации
    path('', HomeView.as_view(), name='home'),  # Главная страниц
    path('register/', RegisterView.as_view(), name='register'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:slug>/subcategories/', SubcategoryListView.as_view(), name='subcategory_list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),


]

