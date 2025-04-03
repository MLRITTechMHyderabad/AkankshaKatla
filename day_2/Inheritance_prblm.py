# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 11:54:14 2025

@author: akank
"""

class Character:
    def __init__(self,name,h,a_pow,defense,speed):
        self.name = name
        self.health = h
        self.attack_power = a_pow
        self.defense = defense
        self.speed = speed
        
    def attack(self,target):
        damage =  self.attack_power - target.defense
        print(self.name ,"attacks", target.name ,"Deals", damage ,"damage.")
        target.take_damage(damage)
        
    def take_damage(self,amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage.")
        if self.health <= 0:
            print(self.name," is defeated!")

    def is_alive(self):
        if self.health <= 0:
            return False
        return True
class Warrior(Character):
    def __init__(self,name,h,a_pow,defense,speed):
        super().__init__(name,h,a_pow,defense,speed)
        self.rage = 0
    def boost_attack(self):
        if self.rage >= 10:
            self.attack_power += 1
    def berserk_mode(self):
        print(self.name, "enters Berserk Mode! Attack power increased.")
        if self.health < 30:
            self.attack_power *= 2
class Mage(Character):
    def __init__(self,mana,name,h,a_pow,defense,speed):
        super().__init__(name,h,a_pow,defense,speed)
        self.mana = mana
    def fireball(self,target):
        if self.mana == 10:
            damage = self.attack_power + 10
            print(f"{self.name} casts Fireball! Deals {damage} damage but loses 5 health.")
            target.take_damage(damage)
            self.health -= 5  
            self.mana -= 10  
        else:
            print(f"{self.name} tried to cast Fireball but lacks mana!")
class Archer(Character):
    def __init__(self,critical_chance,name,h,a_pow,defense,speed):
        super().__init__(name,h,a_pow,defense,speed)
        self.critical_chance = critical_chance
        self.turn_count = 0
    def precision_shot(self,target):
        self.turn_count += 1
        if self.turn_count % 3 == 0:
            damage = (self.attack_power * 2) - target.defense
            print(f"{self.name} lands a Critical Hit! Deals {damage} damage.")
        else:
            damage = max(1, self.attack_power - target.defense)
            print(f"{self.name} fires an arrow! Deals {damage} damage.")
        target.take_damage(damage) 
            

w = Warrior('Thor', 100, 50, 40, 100)
m = Mage(10, 'Gandalf', 90, 60, 90, 90)
a = Archer(10, 'Alex', 80, 120, 80, 110)

fighters = [w, m, a]

n = len(fighters)
for i in range(n):
    for j in range(i + 1, n):
        if fighters[i].speed < fighters[j].speed:
            fighters[i], fighters[j] = fighters[j], fighters[i]
            
# Battle
turn = 0
while True:
    alive_fighters = []
    for f in fighters:
        if f.is_alive():
            alive_fighters.append(f)
    if len(alive_fighters) <= 1:
        break  
    turn += 1
    #print(turn)
    for fighter in alive_fighters:
        if not fighter.is_alive():
            continue
        target = None
        for opponent in alive_fighters:
            if opponent is not fighter:
                target = opponent
                break
        if target is None:
            break
        if isinstance(fighter, Mage):
            fighter.fireball(target)
        elif isinstance(fighter, Archer):
            fighter.precision_shot(target)
        else:
            fighter.attack(target)


winner = None
for f in fighters:
    if f.is_alive():
        winner = f
        break
print(f"{winner.name} wins the battle!")