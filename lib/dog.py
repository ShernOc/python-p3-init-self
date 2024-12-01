#!/usr/bin/env python3

class Dog:
    #we initialize it using the dunder method
    def __init__(self,name,breed="Mutt"):
        self.name = name 
        self.breed = breed
        print(f" Hey {name},this is an interesting concept {breed}")
        
dog =Dog("Daisy", "Terrier")

        
        
        