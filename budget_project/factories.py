import factory
from django.contrib.auth.models import User
from budgets.models import Budget, Transaction


class UserFactory(factory.django.DjangoModelFactory):
    """Create user for test purposes"""

    class Meta:
        """Meta class for user."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BudgetFactory(factory.django.DjangoModelFactory):
    """Create budget instance for test purposes"""

    class Meta:
        """Meta class for Budget."""

        model = Budget

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('word')
    total_budget = '1000.0'


class TransactionFactory(factory.django.DjangoModelFactory):
    """Create transaction instance for test purposes"""

    class Meta:
        """Meta class for Transaction."""

        model = Transaction

    assigned_user = factory.SubFactory(UserFactory)
    budget = factory.SubFactory(BudgetFactory)
    amount = '200.0'
    description = factory.Faker('paragraph')
