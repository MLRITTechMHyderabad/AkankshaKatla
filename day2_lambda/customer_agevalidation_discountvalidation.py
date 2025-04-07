# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 11:47:17 2025

@author: akank
"""

customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

eligible_cust = filter(lambda x : x['age'] >= 18 and x['age'] <= 40, customers)

discount = list(map(lambda d : {
    "name" : d['name'],
    "age" : d['age'],
    "total_purchase" : d["total_purchase"] * (0.90 if d["age"] <= 25 else 0.95)
    },eligible_cust))
print(discount)