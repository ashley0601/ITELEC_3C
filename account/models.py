from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=100)
    _balance = models.FloatField(default=0)

    def display_info(self):
        return f"Account of {self.name} has balance {self._balance}"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.save()
            return f"Deposited {amount}. New balance is {self._balance}"
        return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.save()
            return f"Withdrawn {amount}. New balance is {self._balance}"
        return "Invalid withdrawal. Amount is greater than balance."

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            self.save()
            return f"Balance set to {self._balance}"
        return "Invalid balance. Balance cannot be negative."

    def __str__(self):
        return self.name
        