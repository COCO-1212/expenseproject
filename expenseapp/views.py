from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum

# Create your views here.
from .forms import ExpenseForm
from .models import Expense

# adding an expense via a form submission and redirects to the expense list on success.
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
    total_expense = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0
    return render(request, 'expense_list.html', {'expenses': expenses, 'total_expense': total_expense})


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
    
        
        
