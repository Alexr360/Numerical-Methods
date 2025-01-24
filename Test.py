import random

name = input("Whats your name?\n")
if "tie" in name.lower() or "wei" in name.lower():
    list_of_insults = ["You should actually teach us numerical methods", "Where is my numerical methods", "This doesen't look like numerical methods to me", "Im not hear to learn python", "Please actually teach something useful"]
    print(str(random.choice(list_of_insults)) + " " + name + ".")
else:
    list_of_platitudes = ["How nice you are", "Nice to meet you", "Goodbye"]
    print(str(random.choice(list_of_platitudes)) + " " + name + ".")