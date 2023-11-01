from django.shortcuts import render, redirect,get_object_or_404

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


def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenseapp:expense_list')

    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'edit_expense_view.html', {'form': form})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    
    if request.method == 'POST':
        expense.delete()
        return redirect('expenseapp:expense_list')

    return render(request, 'delete_expense_view.html', {'expense': expense})
    
        
        
