# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 07:02:35 2020

@author: S.Narain Ramaswamy
"""
class Vehicle:
    def __init__(self,capacity):
        self.capacity = capacity
    def Fare(self):
        seat = self.capacity*100
        print(seat)
class Bus(Vehicle):
    def __init__(self,capacity):
        super(). __init__(capacity)
        self.capacity = capacity
    def Fare(self):
        total_fare = (self.capacity*100) 
        total_fare = total_fare + (total_fare*(10/100))
        return total_fare

b = Bus(50)
f = b.Fare()
print(f)
v = Vehicle(50)    
v.Fare()     
    
        