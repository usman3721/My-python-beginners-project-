#   if follower_countA>follower_countB:
#         if guess=="a":
#             return True
#         else:
#             return False
#     elif follower_countB<follower_countA:
#         if guess =="b":
#             return True
#         else:
#             return False
import random

from clear_module import clear 
from game13logo import logo,vs

from gamedata import data
# def get_random_account():
#     return random.choice(data)



# def format_data(account):
#     name=account["name"]
#     description=account["description"]
#     country=account["country"]
#     return f"{name}  a {description}, from {country}"

# def check_answer(guess,a_follower,b_follower):
#     if a_follower> b_follower:
#         return guess=="a"
#     else:
#         return guess=="b"

# def game():
#     score=0
#     game_should_continue=True
#     account_a=get_random_account()
#     account_b=get_random_account()
#     while game_should_continue:
#         account_a=account_b
#         account_b=get_random_account()
#         while account_b==account_a:
#             account_b=get_random_account()
#         (f" compareA: {format_data(account_a)}")
#         print(vs)
#         (f" compareA: {format_data(account_a)}")
#         guess=input("Who has more follwer.Type 'A',OR 'B' ")
#         a_follower_count=account_a["follower_count"]
#         b_follower_count=account_b["follower_count"]
#         is_correct=check_answer(guess,a_follower_count,b_follower_count)
#         clear()
#         print(logo)
#         if is_correct:
#             score+=1
#             print("You are right: currebt score {score}")
#         else:
#             game_should_continue=False
#             print(f"sorry, that is eromg! Final_score{score}")
# game()



def account_data(account):
    """format the account data into a printable form"""
    account_name=account["name"]
    description=account['description']
    country=account["country"]
    count=account["follower_count"]
    return f"{account_name}, a {description}, from {country}"
   
def check_answer(guess,follower_countA,follower_countB):
    """ return if the user got the answer"""
  
    if follower_countA>follower_countB:
        return guess=="a"
    else: 
        return guess=="b"
score=0
#display art
print(logo)
game_continue=True
dataB=random.choice(data)
while game_continue:
    dataA=dataB
    dataB=random.choice(data)  
    if dataA==dataB:
        dataB=random.choice(data)

    print(f"compare A: {account_data(dataA)}")
    print(vs)
    print(f"against B: {account_data(dataB)}")

    guess=input("Who has more follwer.Type 'A',OR 'B' ").lower()
    follower_countA=dataA['follower_count']
    follower_countB=dataB['follower_count']
    is_correct=check_answer(guess,follower_countA,follower_countB)
    #clear()
    #print(logo)
    
        


    #give user feedback on their guiess
    if is_correct: 
        score+=1
        clear()
        print(logo)
        print(f"Yuu are right! current_score{score}")
    else:
        clear()
        print(logo)
        print(f"sorry you are wrong. Final_score{score}")
        game_continue=False
       


#score keeping


#make the guess repeatable

#make the account at position B the next account at position A