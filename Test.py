import random

name = input("Whats your name?\n")
list_of_insults = ["You are a bastard", "You suck", "You should actually teach us numerical methods", "Where is my numerical methods", "This doesen't look like numerical methods to me", "Im not hear to learn python", "Please actually teach something useful"]
print(str(random.choice(list_of_insults)) + " " + name + ".")