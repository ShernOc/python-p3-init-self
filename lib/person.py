#!/usr/bin/env python3

class Person:
    def __init__(self,name):
        self.name = name 
    # to perform an action, and call it 
    def names(self):
        print(f"Hello {self.name}")
    # def __str__(self) -> str:
    #     return f"Person: {self.name}"
        
#create an object 
sherlyne =Person("sherlyne")
sherlyne.names() 

print(sherlyne)
        
        
