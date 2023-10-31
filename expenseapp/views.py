from django.shortcuts import render, redirect

# Create your views here.
from .forms import ExpenseForm
from .models import Expense

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenseapp:expense_list')

    else:
        form = ExpenseForm()

    return render(request, 'add_expense_view.html', {'form': form})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})
