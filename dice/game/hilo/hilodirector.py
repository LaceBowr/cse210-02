#from hilo import Hilo
import random


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[points]): An accumulation or deduction of instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.guesser = Hilo()
        self.is_playing = True
        self.total = 300
        self.first_card = 0
        self.guess = 0
        self.last_card = 0
        

    def random_card(self, exclusions=[]):
        """Displays the first card. Also asks the player for their guess.""" 
        choices = []
        for i in range(1,14):
            if i not in exclusions:
                choices.append(i)
        return random.choice(choices)
        """Args:
            self (Director): An instance of Director.
        """

    def start_game(self):
        """Starts the game by running the main game loop.
        Args:self (Director): an instance of Director.
        """
   
        """Ask the user if they want to play hi/lo?.

        Args:
            self (Director): An instance of Director.
        """
        #print("A card from 1 to 13 will appear and you guess if the next card will be higher or lower.\n" 
        #"You begin with 300 points.\n"
        #"If your Hilo prediction is correct you  add 100 points to your score.\n"
        #"If your Hilo prediciton is incorrect you subtract 75 points from your\n" 
        #"score." )
        play = input("Play Hilo? [y/n] ")
        
        self.is_playing = (play == "y")
        while self.is_playing:
            self.first_card = self.random_card()
            self.guess = self.guesser.guess(self.first_card)
            self.last_card = self.random_card([self.first_card])
            self.score()
            self.end_game()

    def score(self):    
        # Updates the player's score.
        if self.first_card > self.last_card and self.guess == 'l':
            self.total += 100
            print(f"You guessed correct (second card was {self.last_card})! You get 100 points.")
        elif self.first_card < self.last_card and self.guess == 'h':
            self.total += 100
            print(f"You guessed correct (second card was {self.last_card})! You get 100 points.")
        else:
            self.total -= 75
            print(f"You are incorrect (second card was {self.last_card}). You lose 75 points.")
            self.is_playing = input(f"play Hilo? y/n (Your score is: {self.total})")
        if self.is_playing == "n":
                exit()

    def end_game(self):
        if self.total <= 0:
            self.is_playing = False 
            print("Your points are at 0.... sorry, GAME OVER!")

        
    