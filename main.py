from functions import generate_initial_cards, generate_card, check_for_blackjack


first_cards = generate_initial_cards

DEALERS_FACEUP_CARD = first_cards[-1]
Players_initial_cards = first_cards[0]

blackjack = check_for_blackjack(Players_initial_cards)

if blackjack:
    txt = "player wins"
    pass