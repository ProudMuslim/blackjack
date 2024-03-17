import sys
import random
import deck
import time


def first_launch_prompt():
    print(f"""Welcome !!! This is a game of blackjack, don't worry won't be asking for your money 
Let this show you that gambling sucks and you will lose.""")

    first_launch_play_question = input("Would you like to begin or leave ('Y for play N for leave') :  ").strip().lower()
    if first_launch_play_question == "n" or first_launch_play_question == "q":
        sys.exit()
    elif first_launch_play_question == "y":
        return
    else:
        while first_launch_play_question != "q" or first_launch_play_question != "n":
            print("\n\nSeems like you put an invalid input :(, lets try that again. If your 'N' button is broken type 'q' instead, or if your 'y' is broken type 'p' instead\n")
            first_launch_play_question = input("Would you like to begin or leave ('Y/P for play N/Q for leave') :  ").strip().lower()
            if first_launch_play_question == "q" or first_launch_play_question == "n":
                sys.exit()
            elif first_launch_play_question == "y" or first_launch_play_question == "p":
                return


def add_suit_to_deck(suit):
    for card, num in suit.items():
        full_deck.update({card: num})


def rand_card():
    random.shuffle(faces)
    card = random.choice(faces)
    faces.remove(card)
    return card


def hand():
    left_card = rand_card()
    right_card = rand_card()
    return left_card, right_card


def card_value(card):
    return full_deck.get(card)


def main():

    # don't forget to break out of this main while loop
    while True:

        print("Shuffling...")
        # time.sleep(1.5)

        # game begins, player cards given, values unpacked and stored
        value = []
        str_face_cards = ["Ace", "Jack", "Queen", "King"]  # so I can easily refer
        player_right, player_left = hand() # player's hand unpacked
        p_right_value, p_left_value = card_value(player_right), card_value(player_left) # player's hand values unpacked

        # all cards that player is dealt to be unpacked and printed out
        all_player_cards = [player_left,player_right]
        print(*all_player_cards)

        # for if statements, keeping the values, in order to refer easier
        stand_input = ["s","stand"]
        hit_input = ["h", "hit"]

        # officially game begins
        hit_or_stand = input("Hit or stand (H/S) 'type 'q' to quit' : ").lower().strip()
        if hit_or_stand == "q":
            sys.exit()

        # we just managed hmd to add every hit card to the already exisintg cards and showing them all in order
        while hit_or_stand not in stand_input and hit_or_stand in hit_input:
            hit_card = rand_card()
            all_player_cards.append(hit_card)  # putting all the cards together so the hit card can be shown
            print(*all_player_cards)  # printing all cards including the new one that was just hit
            hit_or_stand = input("Hit or stand (H/S) 'type 'q' to quit' : ").lower().strip()
            if hit_or_stand == "q":
                break


suit_ids = {"spade": 0x1F0A0, "hearts": 0x1F0B0, "diamonds": 0x1F0C0, "clubs": 0x1F0D0}
white_card = chr(0x1F0A0)
full_deck = {}

# instantiating a spade object, making the whole suit, and picking a random spade card
spade_suit_obj = deck.Deck("spade", suit_ids.get("spade"))
spade_suit = spade_suit_obj.make_whole_suit()
add_suit_to_deck(spade_suit)

# instantiating a heart object, making the whole suit, and picking a random card
hearts_suit_obj = deck.Deck("hearts", suit_ids.get("hearts"))
hearts_suit = hearts_suit_obj.make_whole_suit()
add_suit_to_deck(hearts_suit)

# instantiating a diamond object, making the whole suit, and picking a random card
diamonds_suit_obj = deck.Deck("diamonds", suit_ids.get("diamonds"))
diamonds_suit = diamonds_suit_obj.make_whole_suit()
add_suit_to_deck(diamonds_suit)

# instantiating a club object, making the whole suit, and picking a random card
clubs_suit_obj = deck.Deck("clubs", suit_ids.get("clubs"))
clubs_suit = clubs_suit_obj.make_whole_suit()
add_suit_to_deck(clubs_suit)


faces = [card for card, num in full_deck.items()]


main()