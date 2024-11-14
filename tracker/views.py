from django.shortcuts import render
from .models import Expense, Income

# Home view

def home(request):
    expenses = Expense.objects.all()  # Assuming you have an Expense model
    incomes = Income.objects.all()    # Assuming you have an Income model
    return render(request, 'tracker/home.html', {'expenses': expenses, 'incomes': incomes})
# View to display a list of expenses
def expense_list(request):
    expenses = Expense.objects.all()  # Fetch all expenses from the database
    return render(request, 'tracker/expense_list.html', {'expenses': expenses})

# View to display a list of incomes
def income_list(request):
    incomes = Income.objects.all()  # Fetch all incomes from the database
    return render(request, 'tracker/income_list.html', {'incomes': incomes})
