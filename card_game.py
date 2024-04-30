import random
import time

def choose_cards(winner_list):
    print("Now Choose the right card ✔")
    print()
    print(winner_list)
    time.sleep(2)
    right_card = random.choice(winner_list)
    
    ask1 = input("Enter the Card number: ")
   
    if ask1.isdigit() and int(ask1) in range(1, len(winner_list) + 1):
        chosen_card = winner_list[int(ask1) - 1]
        if chosen_card == right_card:
            print("Congratulations 🌟 You have selected the right card")
            print()
            print(" ✨✨  YOU HAVE WON THE GAME  ✨✨ ")
        else:
            print("You have selected the wrong card 😭\nYOU LOST")
            print()
    else:
        print("Invalid input! Please enter a number between 1 and", len(winner_list))
        print()

    print("-----------Thanks for Playing----------".center(150))
    print()


def display_list_cards():
    defined_cards=[
    "Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades",
    "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades",
    "King of Spades", "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts",
    "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts",
    "Queen of Hearts", "King of Hearts", "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds",
    "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds",
    "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds",
    "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs",
    "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs"]
    
    global list1, list2, list3
    list1 = [(i+1, defined_cards[i]) for i in random.sample(range(len(defined_cards)), 3)]
    list2 = [(i+1, defined_cards[i]) for i in random.sample(range(len(defined_cards)), 3)]
    list3 = [(i+1, defined_cards[i]) for i in random.sample(range(len(defined_cards)), 3)]
   
    print("Here are the three lists of cards..................")
    time.sleep(2)
    print("1. ", [f"{card[0]}. {card[1]}" for card in list1])
    print()
    print("2. ", [f"{card[0]}. {card[1]}" for card in list2])
    print()
    print("3. ", [f"{card[0]}. {card[1]}" for card in list3])
    print()
    choose_list()

def choose_list():
    ask = int(input("Choose the list by entering its number (1, 2, or 3): "))
    print()
    if ask == 1:
        chosen_list = list1
    elif ask == 2:
        chosen_list = list2
    elif ask == 3:
        chosen_list = list3
    else:
        print("Invalid input! Please enter a number between 1 and 3.")
        return
   
    winner_list = random.choice([list1, list2, list3])
    if chosen_list == winner_list:
        print("Congratulations 🌟 You have selected the right list")
        print()
        choose_cards(winner_list)
    else:
        print("Sorry, you have selected the wrong list. Game Over.")
        print()
        print("-----------Thanks for Playing----------".center(150))

def main_menu():
    wel = " ✨ Welcome to Guess the card Game ✨ "
    print(wel.center(150))
    print()
    print("How to Play : \n\n  1.Choose the right list of card✅\n\n  2.From that list select the right card✅")
    print()
    
    display_list_cards()

main_menu()
