import random  # Importing the 'random' module to enable random selection from a list

# Prompt the user to input their name and store it in the variable 'name'
name = input("What's your name?\n")

# Check if the lowercase version of the inputted name contains the substring "tie" or "wei"
if "tie" in name.lower() or "wei" in name.lower():
    # Create a list of humorous or sarcastic comments about teaching numerical methods
    list_of_insults = [
        "You should actually teach us numerical methods",
        "Where is my numerical methods",
        "This doesn't look like numerical methods to me",
        "I'm not here to learn Python",
        "Please actually teach something useful"
    ]
    # Randomly choose one of the comments from the list and print it with the user's name
    print(str(random.choice(list_of_insults)) + " " + name + ".")
else:
    # Create a list of polite or friendly phrases
    list_of_platitudes = [
        "How nice you are",
        "Nice to meet you",
        "Goodbye"
    ]
    # Randomly choose one of the phrases from the list and print it with the user's name
    print(str(random.choice(list_of_platitudes)) + " " + name + ".")