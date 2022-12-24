import random
from blackjacklogo import logo
from clear_module import clear
def deal_card():
    """ return a random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    """ """
    if sum(cards)==21 and len(cards)==2:
        return 0 #or 11 in cards and 10 in cards
    if 11 in cards and sum(cards)==21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "lose,oponent has a blackjack"
    elif user_score==0:
        return"Won with a balckjack"
    elif user_score>21:
        return "you went over. You lose"
    elif computer_score>21:
        return "Opopnent went over,You win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You won"          
      
playgame=False   
 

def playgame():
    print(logo)

    user_card=[]
    computer_card=[]

    for _ in range(2):
        # new_card=deal_card()
        user_card.append(deal_card()) #+= and extend should not be used, but it can be useful if we want to add  list of items
        computer_card.append(deal_card())
    is_game_over=False
    while not is_game_over:
    
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)

        print(f"Your cars{user_card}, current card is {user_score}")
        print(f"computer's first card {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over=True
        else:
            user_should_deal=input("Type y to get another card, type n to pass ")
            if user_should_deal=="y":
                user_card.append(deal_card())
            else:
                is_game_over=True
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    print(f"Your final hand: {user_card}, final_score {user_score}")
    print(f" Computer final hand {computer_card}, final_score: {computer_score}")
    print(compare(user_score,computer_score))
while input("Do you want to paly the blackajck game again? Type y or n:") =="y":
   
    playgame()
    # clear()



    
