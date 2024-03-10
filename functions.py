import random
import pandas as pd
from Classes import Card, Game_Over_Error



cards_df = pd.read_csv(r"C:\Users\ridle\OneDrive\Desktop\personal_code_projects\Blackjack-Training-Tool\all cards.csv")
cards_dict = cards_df.to_dict()
CARDS_LIST =  list(cards_dict["Card"].values())

def generate_card():
    return Card(random.choice(CARDS_LIST))

#potentially make a function that calculates what the player is allowed to do since this gets used a lot
#i reckon just have a list going of all their decisions and clear it once the hand is over (maybe)

#this function should account for what the player is actually allowed to do
#so if it is their first move, they can do all choices
#if they've split on the first move they can do all choices but split
#if they chose to hit on the first turn they can only hit or stand after that 
#if they've chosen to double then their choices have finished
#etc.

#make this return Card objects
def generate_initial_cards():
    card_sequence = ["player card", "dealer card", "player second card", "dealer face down card"]
    players_random_cards = random.sample(CARDS_LIST, k = 2)
    player_cards = [Card(i) for i in players_random_cards]
    dealers_random_face_up_card = random.sample(CARDS_LIST, k = 1)
    dealers_card = Card(dealers_random_face_up_card[0])
    return player_cards, dealers_card


def card_sum_total(card_list):
    total = 0
    for card in card_list:
        total += card.numeric_value
    return total


#this function should also technically then play the dealer and see if they have a blackjack too
#however in this use case (a perfect strategy training tool) it doesn't really matter since we only care about what the player should do and they can't do anything in this case
def check_for_blackjack(players_cards):
    card_values = [card.numeric_value for card in players_cards]
    return 11 in card_values and 10 in card_values


#this function can only take a list that has 2 card objects in it
def ask_player_turn_split(players_cards):
    pass

def ask_player_turn(players_cards, players_turns):
    #starting cards
    if players_turns == []:
        choice = input("Would you like to Hit (h), Split (p), Double (d) or Stand (s) \n")
    if players_turns == ['s']:
        ask_player_turn_split(players_cards)
    if 'd' in players_turns:
        raise Game_Over_Error
    
def print_card_list(card_list):
    for card in card_list:
        print(card.code)

def play_dealer(dealers_face_up_card):
    #randomly picking the dealers face down card
    dealers_face_down_card = generate_card()
    #list of card objects [card_object 1, card_object 2]
    cards = [dealers_face_up_card, dealers_face_down_card]
    #list of card values [4, 10, "1 or 11"]
    card_values = [card.value for card in cards]
    #this is the numeric sum of the card values. Aces are counted as 11
    total = card_sum_total(cards)

    if 11 not in card_values and total >21:
        print("Dealer Busts")
        print("Player Wins")

    #this code makes an ace go from an 11 to a 1
    elif 11 in card_values and total >= 17 and total <= 21:
        #dealer must stand
        print_card_list(cards)
        print(f"Dealer stands on a total of {total}")


    #this needs to be built better (probably re-written entirely) to accomodate for the possibility of multiple aces being drawn
        #should do one ace at a time and make self.numeric_value = 1 instead of 11
        #then it should rerun card_sum_total(cards)
    elif 11 in card_values and total >21:
        #find first ace and make it's value a 1 instead of 11
        for i in range(len(cards)):
            if cards[i].numeric_value == 11:
                cards[i].numeric_value = 1
                total -= 10
                break
        #dealer must hit
        cards.append(generate_card())
        #then do the whole process again

    




#this is to get built to be the perfect strategy thing
#this should also account for what the player is allowed to do
def what_should_you_do(players_cards, dealers_card):
    pass
