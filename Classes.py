class Card():
    def __init__(self, card_code):
        suits = {"H": "Hearts", "S": "Spades", "C": "Clubs", "D": "Diamonds"}
        Values = {"A": "Ace", "K": "King", "Q": "Queen", "J": "Jack"}
        Numeric_Values = {"Ace": 11, "King": 10, "Queen": 10, "Jack": 10}


        self.suit = suits[card_code[-1]]
        self.code = card_code

        if card_code[0] in Values:
            self.value = Values[card_code[0]]
        else:
            self.value = card_code[0:2].strip("_")
        self.name = f"{self.value} of {self.suit}"

        if self.value in Numeric_Values:
            self.numeric_value = Numeric_Values[self.value]
        else:
            self.numeric_value = int(self.value)

    def __str__(self):
        return self.code
    
class Game_Over_Error(Exception):
    def __init__(self):
        message = f"Game should already be over as the player previously doubled their bet"
        super().__init__(message)