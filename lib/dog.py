#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self, name = "tg", breed = "Mastiff"):
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
        if (type(name) == str and 0 < len(name)< 26):
            self.name = name
        else: 
            print("Name must be string between 1 and 25 characters.")
        
        if breed in approved_breeds:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            
            
    
        
        
    
