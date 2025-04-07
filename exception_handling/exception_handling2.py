# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 14:59:40 2025

@author: akank
"""

class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        
        :param amount: Amount to withdraw
        :return: Remaining balance or error message
        """
        try:
            # TODO: Implement withdrawal logic
            if amount < 0:
                raise ValueError("Value Error: amount cannot be neg")
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient Funds")
        except ValueError as e:
            return str(e)
        # TODO: Handle negative withdrawal amounts
        except InsufficientFundsError as e:
            # TODO: Handle insufficient funds
            return str(e)
        except Exception as e:
            return str(e)
            pass  # TODO: Handle unexpected errors

# Example Usage:
account = BankAccount(100)
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  # Should raise ValueError
