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
#Don't put floating value. It will give ValueError
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n->> "))

moves = [rock, paper, scissors]
computer_choose = random.randint(0,2)

if user_input>2 or user_input<0 :
    print("Invalid input. You lost.")
else:
    print(moves[user_input])
    print(f"Computer Choose: {moves[computer_choose]}")
    if user_input == computer_choose:
        print("It's a Draw")
    elif user_input == 0 and computer_choose == 2:
        print("You Win!")
    elif user_input == 0 and computer_choose == 1:
        print("You lose.")
    elif user_input == 1 and computer_choose == 0:
        print("You Win!")
    elif user_input == 1 and computer_choose == 2:
        print("You lose.")
    elif user_input == 2 and computer_choose == 0:
        print("You lose.")
    elif user_input == 2 and computer_choose == 1:
        print("You Win!")
        
#another logic      
# user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n->> "))

# computer_choose = random.randint(0,2)

# print(f"Computer Choose : {computer_choose}")
# if user_input>2 or user_input<0:
#     print("Invalid input. You lost")
# elif user_input == 0 and computer_choose == 2:
#     print("W")
# elif computer_choose == 0 and user_input == 2:
#     print("L")
# elif computer_choose > user_input:
#     print("L")
# elif user_input > computer_choose:
#     print("W")
# elif user_input == computer_choose:
#     print("Draw")
