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

import matplotlib.pyplot as plt
import io
import base64

#retrieves and summarizes expense data for creating a categorical spending chart.
def infographics(request):
    # Get the data for your categorical spending chart
    spending = Expense.objects.values('category').annotate(total=Sum('amount'))
    
    category_labels = [item['category'] for item in spending]
    category_values = [item['total'] for item in spending]

    # Create the categorical spending chart
    plt.figure(figsize=(8, 6))
    plt.pie(category_values, labels=category_labels, autopct='%1.1f%%', startangle=140)
    plt.title('Categorical Spending Chart')

    # Save the chart as an image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.read()).decode()
    buffer.close()

    return render(request, 'infographics.html', {'chart_image': chart_image})
