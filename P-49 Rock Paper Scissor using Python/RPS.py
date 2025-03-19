import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if(user_input == 'q'):
        quit()

    