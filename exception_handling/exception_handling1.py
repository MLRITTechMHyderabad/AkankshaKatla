# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 11:36:20 2025

@author: akank
"""

def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        if (type(a) not in [int,float]) or (type(b) not in [int,float]) : 
            raise TypeError("invalid input")
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("error: division by 0")
            else:
                return a / b
        elif operator == '%':
            if b == 0:
                raise ZeroDivisionError("division by 0")
            return a % b
        elif operator == '*':
             return a * b
        elif operator == '**':
             return a ** b
        else:
            raise ValueError("Unsupport operator")
    except ZeroDivisionError as e:
        return str(e)
    except ValueError as e:
        return str(e)
    except TypeError as e:
        return str(e)
    except Exception as e:
        return str(e)
# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"
