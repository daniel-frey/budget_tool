from django.test import TestCase, Client, RequestFactory
from budget_project.factories import BudgetFactory, TransactionFactory, UserFactory


class TestBudgetModels(TestCase):
    """Class to test the budget model."""

    def setUp(self):
        """Create the test factory."""
        self.budget = BudgetFactory(
            name='budget',
            total_budget='200.0',
        )

    def test_budget_model(self):
        """Test budget model."""
        self.assertEqual(self.budget.name, 'budget')
        self.assertEqual(self.budget.total_budget, '200.0')


class TestTransactionModels(TestCase):
    """Test the transaction model."""

    def setUp(self):
        """Create a transaction instance for testing."""
        self.transaction = TransactionFactory(
            description='budget'
        )

    def test_transaction(self):
        """Test the transaction"""
        self.assertEqual(self.transaction.description, 'budget')


class TestTransactionViews(TestCase):
    """Test transaction views."""

    def setUp(self):
        """Create instances for testing."""
        self.user = UserFactory()
        self.user.set_password('password')
        self.user.save()
        self.budget = BudgetFactory(user=self.user)
        self.c = Client()
        self.transaction = TransactionFactory(budget=self.budget)

    def test_deny_access_if_not_authenticated(self):
        """Test the redirect if the user is not logged in."""
        res = self.c.get('/budgets/transactions/1', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_transaction_view(self):
        """Test that transactions will be available when logged in."""
        self.c.login(
            username=self.user.username,
            password='password'
        )

        res = self.c.get('/budgets/transactions/' + str(self.transaction.id))
        self.assertIn(self.transaction.amount.encode(), res.content)
        self.assertIn(self.transaction.description.encode(), res.content)


class TestBudgetViews(TestCase):
    """Test the budget views."""

    def setUp(self):
        """Create instances for testing."""
        self.user = UserFactory()
        self.user.set_password('password')
        self.user.save()
        self.c = Client()

    def test_home_route(self):
        """Test the home route."""
        response = self.c.get('')
        assert b'Welcome' in response.content

    def test_access_denied(self):
        """Test that the user must be logged in to see the list view."""
        res = self.c.get('/budgets/budget', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_login_view(self):
        """Test the list route when logged in."""
        self.c.login(
            username=self.user.username,
            password='password'
        )

        budget = BudgetFactory(user=self.user)
        res = self.c.get('/budgets/budget')

        self.assertIn(budget.name.encode(), res.content)

    def test_list_correct_information(self):
        """Test to ensure that the logged  in user only sees their personal information."""
        self.c.login(
            username=self.user.username,
            password='password'
        )

        own_budget = BudgetFactory(user=self.user)
        other_budget = BudgetFactory()

        res = self.c.get('/budgets/budget')

        self.assertIn(own_budget.name.encode(), res.content)
        self.assertNotIn(other_budget.name.encode(), res.content)

    def test_transactions_listed_in_view(self):
        """Test that the budget view also lists the appropriate transactions."""
        self.c.login(
            username=self.user.username,
            password='password'
        )
        budget = BudgetFactory(user=self.user)
        transaction = TransactionFactory(budget=budget)
        res = self.c.get('/budgets/budget')

        self.assertIn(transaction.description.encode(), res.content)
