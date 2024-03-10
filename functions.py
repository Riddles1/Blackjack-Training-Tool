import random
import pandas as pd
from Classes import Card, Game_Over_Error



cards_df = pd.read_csv(r"C:\Users\ridle\OneDrive\Desktop\personal_code_projects\Blackjack-Training-Tool\all cards.csv")
cards_dict = cards_df.to_dict()
CARDS_LIST =  list(cards_dict["Card"].values())

def generate_card():
    return Card(random.choice(CARDS_LIST))




#make all the cards below this Card objects instead of just cards
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

def check_for_blackjack(players_cards):
    card_values = [card.numeric_value for card in players_cards]
    return '1 or 11' in card_values and 10 in card_values

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
    




#this is to get built to be the perfect strategy thing
#this should also account for what the player is allowed to do
def what_should_you_do(players_cards, dealers_card):
    pass
