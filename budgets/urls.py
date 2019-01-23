from django.urls import path
from .views import BudgetView, TransactionView, BudgetCreateView, TransactionCreateView


urlpatterns = [
    path(
        'budget',
        BudgetView.as_view(),
        name='budget_list'),

    path(
        'transactions/<int:id>',
        TransactionView.as_view(),
        name='transaction_detail'),

    path(
        'budget/add',
        BudgetCreateView.as_view(),
        name='add_budget'),

    path(
        'transactions/add/',
        TransactionCreateView.as_view(),
        name='add_transaction')
]
