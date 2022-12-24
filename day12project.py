from random import randint
from guessing import logo
# HARD=10
# EASY=5
# def check_answer(guess,answer,turns):
#     if guess>answer:
#         print("too high")
#         return 
#     elif guess<answer:
#         print("Too low")
#         return 
#     else:
#         print("You got it")
# def set_difficulty():
   
#     level=input("Choose a difficult.Type 'easy' or 'hard'")
#     if level=="easy":
#         return EASY
#     else:
#         return HARD
#     print(HARD)
# set_difficulty()



# def game():
#     answer=randint(1,100) 
#     print(answer)
#     turns=set_difficulty()
#     guess=int(input("make a guess"))
    
#     turns=set_difficulty() 
#     while guess!=answer:
#         turns=turns -1
#         guess=0
#         print("YOu have {turns} left")
#         turns=check_answer(guess,answer,turns)
#         if turns ==0:
#             print("You ran out of guiesses")
#             return
#         elif guess!=answer:
#             print("Guess again")
#     return

# game()










EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def check_answer(answer,guess,turns):
    if guess>answer:
        print("Too high")
        return turns -1
    elif guess<answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it")
def set_difficulty():
    level=input("Choose a difficult.Type 'easy' or 'hard'")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print(logo)
    
    answer=randint(1,100)
    print(answer)
    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempt remaining to guess the number")
        guess=int(input("Make a guess"))
        turns=check_answer(guess,answer,turns)
        if turns ==0:
            print("You ran out of guiesses")
            return
        elif guess!=answer:
            print("Guess again")
game()










