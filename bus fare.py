# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 06:59:31 2020

@author: S.Narain Ramaswamy
"""

class Vehicle:
    def __init__(self,capacity):
        self.capacity = capacity
    def Fare(self):
        totalfare = self.capacity * 100
        return totalfare
class Bus(Vehicle):
    
    def Fare(self):
        totalfare = super().Fare()
        totalfare1 = totalfare + 0.1*(totalfare)
        return totalfare1

b = Bus(50)
f = b.Fare()
print(f)
    
    
        