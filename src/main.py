from functions import generate_initial_cards, play_player, play_dealer

test_cards = generate_initial_cards()
play_player(test_cards[0], test_cards[1])
play_dealer(test_cards[1])