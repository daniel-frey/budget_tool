"""Models for use in the budget app."""
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User


class Budget(models.Model):
    """Budget model has a user as the foreign key, the budget, and a name."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')

    name = models.CharField(max_length=180, default='none')
    total_budget = models.FloatField(default='0.0')
    remaining_budget = models.FloatField(default='0.0')

    def save(self, *args, **kwargs):
        """Make sure that the budget balances."""
        if not self.remaining_budget:
            self.remaining_budget = self.total_budget
        super().save(*args, **kwargs)

    def __repr__(self):
        return '<Budget: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Transaction(models.Model):
    """Transaction model"""
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions', null=True, blank=True)

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transactions')

    STATES = (
        ('WITHDRAWAL', 'Withdrawal'),
        ('DEPOSIT', 'Deposit'),
    )

    type = models.CharField(
        max_length=16,
        choices=STATES,
        default='Withdrawal')

    amount = models.FloatField(default='0.0')
    description = models.CharField(max_length=512, default='transaction')

    def __repr__(self):
            return '<Transaction: {}>'.format(self.description)

    def __str__(self):
        return '{}'.format(self.description)


@receiver(models.signals.post_save, sender=Transaction)
def calculate_remaining_budget(sender, instance, **kwargs):
    """Calculate the remaining budget balance."""
    if instance.type == 'DEPOSIT':
        instance.budget.remaining_budget += instance.amount
    else:
        instance.budget.remaining_budget -= instance.amount

    instance.budget.save()
