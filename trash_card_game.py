""" Final project check in 1
    
"""
from enum import Enum

class Suit(Enum):
    """A Enum class that represents the 4 type of suits of cards.
        Enum reference: https://docs.python.org/3/library/enum.html

    Args:
        Enum (Enum): Enum class as the parent class
    """
    Spade = 1
    Club = 2
    Diamond = 3
    Heart = 4

class Card:
    """ A representation of a crad.
    
    Attributes:
        suit(Suit): The suit of the Card object.
        number(int): The number of the Card object. 11 represents Jack.
                12 represents Queen. 13 represents King.
        revealed(bool): A boolean value represents if the card object 
                has been revealed.
    
    """
    def __init__(self, suit, number, revealed):
        """ Initialize attributes for the card object.

        Args:
            suit (Suit): The suit of the Card object.
            number (int): The number of the Card object. 11 represents Jack.
                12 represents Queen. 13 represents King.
            revealed (bool): A boolean value represents if the card object 
                has been revealed.
                
        Side effects:
            Sets attributes suit, number, and revealed.   
        
        """
        
    def reveal(self):
        """ Set the revealed boolean to Ture to indicate the card has been 
            revealed.
            
        """
        
class Deck:
    """ A deck of cards.
    
    Attributes:
        cards(list): A list of cards.
    
    """
    
    def __init__(self):
        """ Generate a standard deck of 52 cards.
        
        Side effects:
            Set and modify self.cards.
        
        """
        
    def shuffle():
        """ Randomly shuffle the list of cards.
        
        Side effects:
            Modify self.cards
        
        """
        
    def deal():
        """ Get the last card from the list of cards. 
        
        Return: 
            Card: 
        
        
        """
    
    
class Player:
    """[summary]
    """

    def __init__(self):
        
        
class GameStage(Enum):
    """A Enum class that represents the 4 type of game stages.

    Args:
        Enum (Enum): Enum class as the parent class.
        
    """
    Player1Stage = 1
    Player2Stage = 2
    Player1Won = 3
    Player2Won = 4
        

class Game:
    """[summary]
    """
    
    def __init__(self):
        
        
        

        
    