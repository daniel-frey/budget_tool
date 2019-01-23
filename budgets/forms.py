from django.forms import ModelForm
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    """Create the form to add a budget item"""
    class Meta:
        """Meta class for the budget form."""
        model = Budget
        fields = ['name', 'total_budget']


class TransactionForm(ModelForm):
    """Create the form to add a budget item."""
    class Meta:
        """Meta class for the transaction form."""
        model = Transaction
        fields = ['assigned_user', 'budget', 'type', 'amount', 'description']
