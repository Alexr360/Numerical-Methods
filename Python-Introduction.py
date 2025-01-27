import random  # Importing the 'random' module to enable random selection from a list

# Prompt the user to input their name and store it in the variable 'name'
name = input("What's your name?\n")

# Create a lisAlet of polite or friendly phrases
list_of_platitudes = [
    "How nice you are",
    "Nice to meet you",
    "Good Morning"
]
# Randomly choose one of the phrases from the list and print it with the user's name
print(str(random.choice(list_of_platitudes)) + " " + name + ".")