import random
import colorama
from game.player import Player

#Commented
class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        player (Player): An instance of the class of objects known as Player.
        cards (List): The deck of the 13 cards.
        one_card (int): Use to keep track of the value from the displayed card.
        what_you_deserve (int) Represents the points earned or lost in each round
    """

#Commented
    def __init__(self):
        """The class constructor.
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.player = Player("Dear student")
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.one_card = 0
        self.what_you_deserve = 0
        colorama.init()
        
#Commented
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            
#Commented
    def get_a_card(self):
        """Picks up a card from the deck, storing its value and removing it from the list
        Args:
            self (Director): an instance of Director.
        """
        if (len(self.cards) > 0):
            self.one_card = random.choice(self.cards)
            self.cards.remove(self.one_card)
        else:
            print(colorama.Fore.RED +"There are no more cards in the deck!"+ colorama.Fore.RESET)

#Commented
    def can_play(self):
            """Determines whether or not the player can play.
            Args:
                self (player): An instance of Player.
            Returns:
                boolean: True if the deck has cards and the player more than zero points.
                Otherwise, it returns false.
            """
            if (len(self.cards) > 0) and (self.player.able_to_play()):
                return True
            else:
                return False

#Commented
    def get_inputs(self):
        """Gets the value of the obtained card, and the answer from the player guessing if
        the next card will have a higher or lower value.
        Args:
            self (Director): An instance of Director.
        """
        # called the first time to show a card and stored its value
        if len(self.cards) == 13:
            self.get_a_card()
            print()
        
        # stores the previous and current card, and prompts and recieves the answer from the player
        previous_card = self.one_card
        print(colorama.Fore.YELLOW +f"The previous card was: {previous_card}"+ colorama.Fore.RESET)
        answer = self.player.choose_if_hi_lo()
        self.get_a_card()
        current_card = self.one_card
        print(colorama.Fore.YELLOW +f"The next card is: {current_card}"+ colorama.Fore.RESET)

        # calculates the points the player deserves
        if (answer == "h") and (current_card > previous_card):
            self.what_you_deserve = 100
        elif (answer == "l") and (current_card < previous_card):
            self.what_you_deserve = 100
        else:
            self.what_you_deserve = -75

#Commented
    def do_updates(self):
        """Updates the score obtained from the points a player has.
        Args:
            self (Director): An instance of Director.
        """        
        self.player.points += self.what_you_deserve

#Commented
    def do_outputs(self):
        """Outputs the game information for each round, including the Score,
        a prompt for the player to continue playing, and a message to choose y you
        want to leave the game.

        Args:
            self (Director): An instance of Director.
        """
        # if calculations throw a negative score, set it to zero
        if self.player.points < 0:
            self.player.points = 0

        print(colorama.Fore.BLUE +f"Your score is: {self.player.points}"+ colorama.Fore.RESET)

        # If this object can play...
        if self.can_play():
            while True:
                choice = input(f"'{self.player.name}', do you want to continue playing? [y/n] ")
                if choice.lower() == "y":
                    print()
                    print("...")
                    print()
                    self.keep_playing = True
                    break
                elif choice.lower() == "n":
                    print()
                    print(colorama.Fore.GREEN +"The game is over!!"+ colorama.Fore.RESET)
                    print(colorama.Fore.GREEN +"Thanks to test our game!"+ colorama.Fore.RESET)
                    print()
                    self.keep_playing = False     
                    break
                else:
                    print(colorama.Fore.RED +"Please answer the question with a right option!"+ colorama.Fore.RESET)
        else:
            print()
            print(colorama.Fore.GREEN +"The game is over!!"+ colorama.Fore.RESET)
            print(colorama.Fore.GREEN +"Thanks to test our game!"+ colorama.Fore.RESET)
            print()
            self.keep_playing = False