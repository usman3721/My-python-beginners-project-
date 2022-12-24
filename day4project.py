



import random

rock="""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper="""     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# userchoice=input("what did you chooddr type 0 fir rock, 1 for paper, 2 for scissors")
# map=[rock,paper,scissors]
# computer_choice=random.choice(map)
                
# if userchoice==computer_choice:
#      print(userchoice)
#      print(f"computer choosed{computer_choice}")
#      print("You win the game")
# else:
#       print("You loose the game")
# game_image=[rock,paper,scissors]
# user_choice=int(input("what did you want to choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
# if user_choice>=3 or user_choice<0:
#       print("You type an invalid number.You loosed")
# else:
#       print(game_image[user_choice])
# computer_choice=random.randint(0,2)
# print(f"Computer choosed {computer_choice}")
# print(game_image[computer_choice])
# if user_choice==0 and computer_choice==2:
#       print("you win")
# elif computer_choice==0 and user_choice==2:
#       print("You loose")
# elif computer_choice>user_choice:
#       print("You loose")
user_input=int(input("what did you want to type.Type 0 for paper?, 1 for rock 2 for scissor? "))
game_image=[rock,paper,scissors]
computer_user=random.randint(0,2)
if user_input>=3 and user_input<0:
      print("sorry you typed an invaled number. You loose!")
else:
      print(game_image[user_input])
      print(f"The computer choose {computer_user}")
      print(game_image[computer_user])
      if user_input==0 and computer_user==2:
            print("You win the game")
      elif computer_user==2 and user_input==0:
            print("Ypu loose the game")
      elif computer_user> user_input:
            print("You loose")