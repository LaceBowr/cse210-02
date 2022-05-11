import random

"""class Hilo:"""
    
# 2) Create the class constructor. Use the following method comment.
    #Constructs a new instance of cards with a value and points attribute between 1-13.
    """def __init__(self):#Args:self (hilo): An instance of hilo."""            
    
    #Attributes:
        """self.first_card = None
        self.total = 300"""

# 3) Create the (self) method. Use the following method comment.
    #imports a new random card and then asks the player if they guess "high" or "low"
    # then after guessing import a new random card.
    """def guess(self, first_card):"""
        # The responsibility of the guesser is to determine if the last_card is higher or lower and input that data 
        # but their goal is to guess with some form of predictability so that the 
            """self.first_card = first_card 
            self.card_guess = input(f" The first card is {self.first_card}. Do you guess the next card to be higher or lower? (h/l): ") 
            return self.card_guess"""
