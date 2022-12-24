hangman_pics = ['''
+---+
| |
|
|
|
|
=========''', '''
+---+
| |
O |
|
|
|
=========''', '''
+---+
| |
O |
| |
|
|
=========''', '''
+---+
| |
O |
/| |
|
|
=========''', '''
+---+
| |
O |
/|\ |
|
|
=========''', '''
+---+
| |
O |
/|\ |
/ |
|
=========''', '''
+---+
| |
O |
/|\ |
/ \ |
|
=========''']
print()
from hangman_stages import word_list
from hangman_logo import logo
import random
from clear_module import sleep,clear
print(logo)
print("WELCOME TO HANGMAN GAME ")

chosen_word=random.choice(word_list)

print(f"The chosen word is {chosen_word}")
word_lenght=len(chosen_word)
display=[]
lives=6
for _ in range(word_lenght):
    display+="_"



end_of_game=False
while not end_of_game:
    guess=input("Guess a letter? ").lower() 
    if guess in display:
        print(f"You guessed {guess} and you have already guessed the number before ")   
    for position in range(word_lenght):
        letter=chosen_word[position]
        # print(f"Current position: {position}\n current letter: {letter}\n Guessed letter {guess}\n  {lives}")
        if letter==guess:
            display[position]=letter
    print(display)    
    if guess not in chosen_word:
        print(f" {guess} is not in the chosen word")
        lives-=1
        print(f"{lives}")
        if lives==0:
            print("You lose")
    print(f"{''.join(display)}")
    if "_"  not in display:
        end_of_game=True
        print("You won")
    print(hangman_pics[lives])
    sleep(3)
    clear()
    



     


# guess=input("Guesss a letter: ").lower()
# display=[]
# end_of_game=False
# while not end_of_game:
# # guess=input("Guesss a letter: ").lower()
#     for char in chosen_word:  #a;ternatively for _ in range(len(chosen_word)):
#         if char == guess: 
#                 display.append(char)
#         else:                            
#                 display.append("_")
#     print(display)
#     if "_" not in display:
#         end_of_game=True
#         print("You win")









