"""URLs for auth using Django REST framework."""
from .views import RegisterApiView, UserApiView, BudgetListApiView, BudgetDetailApiView, TransactionListApiView, TransactionDetailApiView
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('user/<int:pk>', UserApiView.as_view(), name='user-detail'),
    path('register', RegisterApiView.as_view(), name='register'),
    path('login', views.obtain_auth_token),
    path('budget/', BudgetListApiView.as_view(), name='budget-list-api'),
    path('budget/<int:pk>', BudgetDetailApiView.as_view(), name='budget-detail-api'),
    path('transaction/', TransactionListApiView.as_view(), name='transaction-list-api'),
    path('transaction/<int:pk>', TransactionDetailApiView.as_view(), name='transaction-detail-api'),
]
