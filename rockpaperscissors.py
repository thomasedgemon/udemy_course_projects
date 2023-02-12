import random
import numpy as np
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

options = [rock, paper, scissors]
user_choice = input("What do you choose, R, P, or S? ")
if user_choice == "R":
    print(rock)
elif user_choice == "P":
    print(paper)
elif user_choice == "S":
    print(scissors)

computer_options = [rock, paper, scissors]
computer_choice = np.random.choice(computer_options)
print(f'the computer chose {computer_choice}')

if computer_choice == rock:
    print("computer chose rock")
elif computer_choice == paper:
    print("computer chose pape" )
elif computer_choice == scissors:
    print("computer chose scissors")



if user_choice == "R":
    if computer_choice == rock:
        print("it is a tie.")
    elif computer_choice == paper:
        print("you win!")
    elif computer_choice == scissors:
        print("you lose!")

if user_choice == "P":
    if computer_choice == rock:
        print("you lose!")
    elif computer_choice == paper:
        print("it is a tie")
    elif computer_choice == scissors:
        print("you lose!")

if user_choice == "S":
    if computer_choice == rock:
        print("you lose!")
    elif computer_choice == paper:
        print("You win!")
    elif computer_choice == scissors:
        print("it is a tie.")

