import random

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
#don't put float value then it will give value error. put int value only
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n->> ")) 

if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input ==2:
    print(scissors)
else:
    print("You have put wrong number. You lost!")

set1 = [rock, paper, scissors]
rand_number = random.randint(0,2)
computer_choose = set1[rand_number]
if user_input>=0 and user_input<=2:
    print("Computer choose :- ")
    print(computer_choose)

    if user_input == rand_number:
        print("Draw")
    elif (user_input == 0) and (rand_number == 1):
        print("Lost")
    elif (user_input == 0) and (rand_number == 2):
        print("Win")
    elif (user_input == 1) and (rand_number == 0):
        print("Win")
    elif (user_input == 1) and (rand_number == 2):
        print("Lost")
    elif (user_input == 2) and (rand_number == 0):
        print("Lost")
    elif (user_input == 2) and (rand_number == 1):
        print("Win")
