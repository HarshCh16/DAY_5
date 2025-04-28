#ascii art

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
#main code

import random

symbols = [rock , paper , scissors]
system_choice = random.choice(symbols)

user_input =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user_input_choice = symbols[user_input]

print("YOUR CHOICE = \n")
print(user_input_choice)

print("SYSTEM CHOICE = \n")
print(system_choice)

if user_input_choice == rock :
    if system_choice == scissors :
        print("Rock beats scissors. YOU WON!")
    elif system_choice == paper :
        print("Paper beats scissors. YOU LOSE.")
    else :
        print("Rock and rock. It\'s a tie.")    

if user_input_choice == paper :
    if system_choice == scissors :
        print("Scissors beat paper. YOU LOSE.")
    elif system_choice == paper :
        print("Paper and paper. It\'s a tie.")
    else :
        print("Paper beats rock. YOU WON!")

if user_input_choice == scissors :
    if system_choice == scissors :
        print("Scissors and scissors. It\'s a tie.")
    elif system_choice == paper :
        print("Scissors beats paper. YOU WIN!.")
    else :
        print("Rock beats scissors. YOU LOSE.")