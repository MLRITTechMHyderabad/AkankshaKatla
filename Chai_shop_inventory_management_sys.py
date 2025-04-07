# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 09:41:03 2025

@author: akank
"""

from abc import ABC, abstractmethod
class Chai(ABC):
    def __init__(self,name,quantity_in_stock,base_price):
        self.name = name
        self.quantity_in_stock = quantity_in_stock
        self.base_price = base_price
    @abstractmethod
    def calculate_price(self):
        pass
    @abstractmethod
    def display_info(self):
        pass
class MasalaChai(Chai):
    def __init__(self,name,quantity_in_stock,base_price):
        super().__init__(name,quantity_in_stock,base_price)
    def calculate_price(self):
        m_price = self.base_price + 10
        return m_price
    def display_info(self):
        print(f'Name: {self.name} | Price per cup: {self.base_price} | Stock: {self.quantity_in_stock}')
    
class GingerChai(Chai):
    def __init__(self,name,quantity_in_stock,base_price):
        super().__init__(name,quantity_in_stock,base_price)
    def calculate_price(self):
        g_price = self.base_price + 8
        return g_price
    def display_info(self):
        print(f'Name: {self.name} | Price per cup: {self.base_price} | Stock: {self.quantity_in_stock}')
    
class ElaichiChai(Chai):
    def __init__(self,name,quantity_in_stock,base_price):
        super().__init__(name,quantity_in_stock,base_price)
    def calculate_price(self):
        e_price = self.base_price + 12
        return e_price
    def display_info(self):
        print(f'Name: {self.name} | Price per cup: {self.base_price} | Stock: {self.quantity_in_stock}')
    
class ChaiInventory():
    def __init__(self):
        self.lst = []
    def add_chai(self,chai_obj):
         self.lst.append(chai_obj)
    def show_inventory(self):
        for i in self.lst:
            i.display_info()
    def get_total_inventory_value(self):
        total = 0
        for i in self.lst:
            total += i.calculate_price() * i.quantity_in_stock
        return total

inventory = ChaiInventory() 
chai1 = MasalaChai("Masala chai", 50,10)
chai2 = GingerChai("Ginger Chai", 40, 18)
chai3 = ElaichiChai("Elaichi Chai", 25, 30)


inventory.add_chai(chai1)
inventory.add_chai(chai2)
inventory.add_chai(chai3)

inventory.show_inventory()
print("Total Inventory Value:",inventory.get_total_inventory_value())
