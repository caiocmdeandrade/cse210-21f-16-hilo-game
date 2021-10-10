import colorama

#Commented
class Player:
    """A code template for a person who plays the game. The responsibility of 
    this class of objects is to answer what range they believe the cards numbers will have and if
    they can play another round. 
    
    Attributes:
        name (string): Stores the name of the player.
        points (int): Determines the initial points for the player.
    """

#Commented
    def __init__(self, name):
        """The class constructor.
        Args:
            self (Player): an instance of Player.
        """
        self.name = name
        self.points = 300
        colorama.init()

#Commented
    def choose_if_hi_lo(self):
        """Prompt the user to choose whether the value of the next card will be higher or lower.
        Args:
            self (Player): An instance of Player.
        Return:
            option (String): Represents the answer from the player that is passed to the director class
        """
        while True:
            option = input("Will the next card be higher or lower? [h/l]: ")
            if option.lower() == "h" or option.lower() == "l":
                break
            else:
                print(colorama.Fore.RED +"Please answer the question with a right option!"+ colorama.Fore.RESET)
                print()
        return option
        
#Commented
    def able_to_play(self):
            """Determines whether or not the Player can play again.
            Args:
                self (Player): An instance of Player.
            Returns:
                boolean: True if the player's points are greater than zero. Otherwise, it returns false.
            """
            if self.points > 0:
                return True
            else:
                return False