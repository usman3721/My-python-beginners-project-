from clear_module import clear
from auction_Logo import logo 

print(logo) 

             




print("Welcome to secret auction ")
bids={}

def find_highest_bidder(bidding_record):
    highest_bidder=0
    winner=""
    print(bidding_record)
    for key in bidding_record:
        bid_amount=bidding_record[key]
        print(bid_amount)
        if bid_amount>highest_bidder:
            highest_bidder=bid_amount
            winner=key
    print(f"The winner is {winner} with a bid {highest_bidder} ")

bidding_finish=False
while not bidding_finish:
    name=input("What is your name")
    price=int(input("What is your biding price $"))
    bids[name]=price
    should_continue=input("Are there any other bids, Type 'yes' or 'no' ")
    if should_continue== "no":
        bidding=True
        find_highest_bidder(bids)    
    else:
        clear()
             


