"""Views to handle auth with Django REST framework."""
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import UserSerializer, User, BudgetSerializer, Budget, TransactionSerializer, Transaction


class RegisterApiView(generics.CreateAPIView):
    """View for registering a new user."""
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserApiView(generics.RetrieveAPIView):
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class BudgetListApiView(generics.ListCreateAPIView):
    """Display a list of budgets"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.username)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class BudgetDetailApiView(generics.RetrieveAPIView):
    """Detail view of a single transaction"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.username)


class TransactionListApiView(generics.ListCreateAPIView):
    """Display a list of all transactions"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)


class TransactionDetailApiView(generics.RetrieveAPIView):
    """Detail view of a single transaction"""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)
