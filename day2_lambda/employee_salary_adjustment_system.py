# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:14:49 2025

@author: akank
"""

employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]

sal = list(map(lambda emp: {
    "name": emp["name"],
    "salary": round(emp["salary"] * (1.1 if emp["rating"] == 4 or emp["rating"] == 5 else 1.05 if emp["rating"] == 3 else 0.97),2),
    "rating": emp["rating"]
},employees))

print(sal)

