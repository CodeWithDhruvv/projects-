import random

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

input_by_user = (int (input("What do you chose? Type 0 for rock, 1 for paper or 2 for scissor\n")))
playable_options = ["rock","paper","scissors"]

if playable_options[input_by_user] == "rock":
    print (rock)

if playable_options[input_by_user] == "paper":
    print (paper)

if playable_options[input_by_user] == "scissors":
    print (scissors)

random_selection = random.randint(0,2)

computer_input = playable_options[random_selection]
print ("Computer chose:\n")
if computer_input == "rock":
    print (rock)
    print("\n")
if computer_input == "paper":
    print (paper)
    print("\n")
if computer_input == "scissors":
    print (scissors)
    print("\n")

# to decide if person wins or looses

if computer_input == playable_options[input_by_user]:
    print("Tie")

if computer_input == "rock" and playable_options[input_by_user] == "paper":
    print ("You win")
if computer_input == "rock" and playable_options[input_by_user] == "scissors":
    print ("You lose")

if computer_input == "paper" and playable_options[input_by_user] == "scissors":
    print ("You win")
if computer_input == "paper" and playable_options[input_by_user] == "rock":
    print ("You lose")

if computer_input == "scissors" and playable_options[input_by_user] == "rock":
    print ("You win")
if computer_input == "scissors" and playable_options[input_by_user] == "paper":
    print ("You lose")














