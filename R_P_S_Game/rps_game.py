"""Rock Paper Scissors Game"""
import random
ROCK = '''
  .----.-----.-----.-----.
 /      \     \     \     \\
|  \/    |     |   __L_____L__
|   |    |     |  (           \\
|    \___/    /    \______/    |
|        \___/\___/\___/       |
 \      \     /               /
  |                        __/
   \_                   __/
    |        |         |
    |                  |
    |                  |
'''
PAPER = '''
            .-.                 
            |U|    _      
        _   | |   /<)     
       (>\  | |  / /
        \ \ | | / / .-.
         \ \| |/ /.'`.'
          \     `' .'
    .---. |       /      
    `--. `'       |    
        \         /
         |       |     
'''
SCISSORS = '''
   ____
  / __ \\
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''
game_images = [ROCK, PAPER, SCISSORS]
user_choice = int(input("What do you choose? "
                        "Type 0 for Rock, "
                        "1 for Paper, "
                        "2 for Scissors - \n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you loose! ")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("Congratulations, You win! ")
    elif computer_choice == 0 and user_choice == 2:
        print("Sorry, You loose! ")
    elif computer_choice > user_choice:
        print("Sorry, You loose! ")
    elif user_choice > computer_choice:
        print("Congratulations, You win! ")
    elif computer_choice == user_choice:
        print("It's a draw! ")
