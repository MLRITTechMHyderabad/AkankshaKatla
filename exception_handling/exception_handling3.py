# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 21:26:32 2025

@author: akank
"""

def process_data(data, index):
    """
    Processes data with error handling.
    
    :param data: List of numbers (strings that should be converted to int)
    :param index: Index to divide with
    :return: Processed result or error message
    """
    try:
        # TODO: Convert elements to integers
        # TODO: Perform division
        int_data = [int(i) for i in data]
        
        div = int_data[index]
        res = int_data[0] / div
        return res
    except ZeroDivisionError:
        return 'Zero division error: cannot divide by 0'  # TODO: Handle division by zero
    except ValueError:
        return 'Value Error'  # TODO: Handle invalid conversions
    except IndexError:
        return 'Index out of range'  # TODO: Handle out-of-bounds index
    except Exception as e:
        return str(e)  # TODO: Handle unexpected errors

# Example Usage:
data_list = ["10", "20", "0", "40"]
print(process_data(data_list, 2))  # Should handle division by zero
print(process_data(["10", "abc", "30"], 1))  # Should handle ValueError
print(process_data([10, 20], 5))  # Should handle IndexError

