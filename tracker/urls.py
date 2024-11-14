from django.urls import path
from . import views

urlpatterns = [
    path('expenses/', views.expense_list, name='expense_list'),  # URL for viewing expenses
    path('income/', views.income_list, name='income_list'),  # URL for viewing income
    path('', views.home, name='home'),
]

