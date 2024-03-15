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
def check_for_blackjack(cards):
    if len(cards) == 2:
        card_types = [card.value for card in cards]
        numerics = [card.numeric_value for card in cards]

        return ("Ace" in card_types and 10 in numerics)
    return False


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
    print(f"Dealers Cards are {[i.code for i in cards]}")
    #list of card values [4, 10, "1 or 11"]
    card_values = [card.value for card in cards]
    #this is the numeric sum of the card values. Aces are counted as 11
    total = card_sum_total(cards)
    while True:        
        if total >= 17 and total <= 21:
            #dealer must stand
            print(f"Dealers cards are {[i.code for i in cards]}")
            print(f"Dealer stands on a total of {total}")
            return total
        
        if 11 not in card_values and total >21:
            #dealer busts

            print(f"Dealer busts on a total of {total}")
            print("Player Wins")
            return total

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
            for i in range(len(card_values)):
                if card_values[i] == 11:
                    card_values[i] == 1
                    break
            
            #dealer must hit
            cards.append(generate_card())
            total += cards[-1].numeric_value
            #then do the whole process again

        if total <17:
            new_card = generate_card()
            cards.append(new_card)
            total += cards[-1].numeric_value
            card_values.append(new_card.value)
            print("Dealer hits")
            print(f"Dealers cards are {[i.code for i in cards]}")

def ask_hsdp():
    choices = ['h', 's', 'd', 'p']
    while True:
        choice = input("What would you like to do? h(hit), s(stand), d(double), p(split)")
        if choice in choices:
            return choice
        else:
            print("Please pick a valid choice")

def ask_hsd():
    choices = ['h', 's', 'd']
    while True:
        choice = input("What would you like to do? h(hit), s(stand), d(double)")
        if choice in choices:
            return choice
        else:
            print("Please pick a valid choice")




def play_hand(cards):
    pass


def play_player(players_cards):
    hands = [players_cards]
    finishing_hands = []

    def choice_handler(hand, choice):
        if choice == 'h':
            print("hitting")
            hand.append(generate_card())
        if choice == 's':
            print("standing")
        if choice == 'd':
            hand.append(generate_card())
        if choice == 'p':
            print("splitting")
            hands.append([hand.pop()])
################################################################################################# working on this atm (check for 21 (atm the game asks player what they want to do on a total of 21)) (fix double ace problem of making 11's into 1's because 11 + 11 > 21)
    for hand in hands:
        while True:
            total = card_sum_total(hand)
            hand_values = [card.numeric_value for card in hand]
            hand_value = [card.value for card in hand]

            #if the hand only contains 1 card (player just split) add a new card to that hand
            if len(hand) == 1:
                if hand[0].value == "Ace":
                    hand[0].numeric_value = 11
                hand.append(generate_card())
                total = card_sum_total(hand)
            #checking for blackjack
            if check_for_blackjack(hand):
                print("Blackjack. PLayer wins")
                finishing_hands.append(hand)
                break
            #checking for 21 with new card          
            if total == 21:
                print(f"Your Cards:\n{[card.value for card in hand]}")
                print("Player wins with 21")
                finishing_hands.append(hand)
                break
            #check for 21 with as new card
            if hand[0].value == "Ace":
                if (total - 10) == 21:
                    print(f"Your Cards:\n{[card.value for card in hand]}")
                    print("Player wins with 21")
                    finishing_hands.append(hand)
                    break       



            if 11 not in hand_values and total >21:
                print(f"Your Cards:\n{[card.value for card in hand]}")
                print(f"Player busts on a total of {total}")
                finishing_hands.append(hand)
                break
            #find first ace and make it's value a 1 instead of 11
            elif 11 in hand_values and total >21:
                for i in range(len(hand)):
                    if hand[i].numeric_value == 11:
                        hand[i].numeric_value = 1
                        total -= 10
                        break
                for i in range(len(hand)):
                    if hand[i] == 11:
                        hand[i] == 1
                        break         

            if hand[0].value == hand[1].value and len(hand) == 2:
                print(f"Your Cards:\n{[card.value for card in hand]}")
                choice = ask_hsdp()
                choice_handler(hand, choice)
                if choice == "s":
                    print(f"Player stands on {total}")
                    finishing_hands.append(hand)
                    break
                if choice == "d":
                    print("Player doubles")
                    print(f"Your Cards:\n{[card.value for card in hand]}")
                    total += hand[-1].numeric_value
                    if total >21:
                        print("player busts")
                        finishing_hands.append(hand)
                        break
                    else: 
                        print(f"player finishes on a total of {total}")
                        finishing_hands.append(hand)
                        break
            elif (len(hand) != 2) or (len(hand) > 1 and hand[0].value != hand[1].value):
                print(f"Your Cards:\n{[card.value for card in hand]}")
                choice = ask_hsd()
                choice_handler(hand, choice)
                if choice == "s":
                    print(f"Player stands on {total}")
                    finishing_hands.append(hand)
                    break
                if choice == "d":
                    print("Player doubles")
                    print(f"Your Cards:\n{[card.value for card in hand]}")
                    total += hand[-1].numeric_value
                    finishing_hands.append(hand)
                    break


    finishing_hand_codes = []
    for hand in finishing_hands:
        finishing_hand_codes.append([card.code for card in hand])
    print("Players hands:")
    for hand in finishing_hand_codes:
        print(hand)
    return finishing_hands
        


#this is to get built to be the perfect strategy thing
#this should also account for what the player is allowed to do
def what_should_you_do(players_cards, dealers_card):
    players_card_values = [card.value for card in players_cards]
    players_numeric_values = [card.numveric_value for card in players_cards]
    card_sum_total = card_sum_total(players_cards)
    player_has_ace = "Ace" in players_card_values

    if player_has_ace:
        #refer to has ace part of the table
        #it should be ace + total
        #so ace, 4, 2, 7 would just be ace + 13
        pass
    else:
        #refer to doesn't have ace part of the table
        pass
    


forced_splitting_opportunity_card_list = [Card("A_C"), Card("A_H")]
forced_blackjack_card_list = [Card("A_S"), Card("J_H")]

initial_cards = generate_initial_cards()
play_player(forced_splitting_opportunity_card_list)