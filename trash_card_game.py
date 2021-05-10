""" Final project check in 1

"""
from argparse import ArgumentParser
import sys
import random
import time
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
    def __init__(self, suit, number, revealed = False):
        """ Initialize attributes for the card object.

        Args:
            suit (Suit): The suit of the Card object.
            number (int): The number of the Card object. 11 represents Jack.
                12 represents Queen. 13 represents King.
            revealed (bool, optional): A boolean value represents if the card
                object has been revealed. Defaults to False.

        Side effects:
            Sets attributes suit, number, and revealed.
        """
        self.suit = suit
        self.number = number
        self.revealed = revealed

    def reveal(self):
        """ Set the revealed boolean to True to indicate the card has been
            revealed.

        Side effects:
            Sets attribute revealed.
        """
        self.revealed = True
        
    def __str__(self):
        if self.revealed:
            return f"{self.number} {self.suit.name}"
        else:
            return "*"

class Deck:
    """ A deck of cards.

    Attributes:
        cards(list): A list of cards.

    """

    def __init__(self):
        """ Generate a standard deck of 52 cards and shuffle.

        Side effects:
        Set attributes cards.

        """
        self.cards = []
        self.build_deck()

    def build_deck(self):
        """ Build a deck

        Side effects:
            Modify self.cards.

        """
        for suit in Suit:
            for number in range(1,14):
                self.cards.append(Card(suit, number))
        self.shuffle()

    def shuffle(self):
        """ Randomly shuffle the list of cards.

        Side effects:
            Modify self.cards

        """
        random.shuffle(self.cards)

    def deal(self, count = None):
        """ Get the last card from the list of cards.

        Args:
            count (int): The number of cards need to be dealed.

        Return:
            Card: The last card from the list of cards.

        Raises:
            ValueError: No card in cards or not enough cards to be dealed.

        Side effects:
            Modify self.cards

        """

        if self.cards == None or len(self.cards) == 0:
            raise ValueError("incorrect cards value.")

        if count == None: # if there is no count input, reveal the card after
            # the dealing of card
            card = self.cards.pop()
            card.reveal()
            return card
        else:
            if len(self.cards) < count:
                raise ValueError("Not enough cards.")

            dealed_cards = []
            for i in range(count):
                dealed_cards.append(self.cards.pop())
            return dealed_cards

class Player:
    """ A class of player information with name, the list of the cards of the
        player and the card in the hand of the player.

    Attributes:
        name (str): name of player.
        position_cards (list): A list of Card objects representing the cards
            a player has for the game. Initially, the player has 10 unrevealed
            cards.
        card_in_hand (Card): a card the player is dealt from the deck or from 
            the disposed pool for making different decisions including swapping 
            with one of the card from the cards of the player and disposing the 
            card which will append the card to the disposed pool.

    """

    def __init__(self, name, position_cards, card_in_hand = None):
        """ Initialize the player with a name, list of the cards of the player
            and an optional card in hand.

        Args:
            name (name): The name of the player.
            position_cards (list): A list of 10 unrevealed Card objects
                representing the cards a player initially has for the game.
            card_in_hand (Card, optional): A Card object representing the card 
                the player has in hand to play the game. Defaults to None.

        """
        self.name = name
        self.position_cards = position_cards
        self.card_in_hand = card_in_hand
        
    def check_swap(self, index):
        """ Check whether it is possible to swap a card in hand with a position 
            card. If the cards can be swapped, return True. Otherwise return 
            False.
        
        Args:
            index (int): The index of the card in the cards attribute that the
            card in hand is trying to swap.

        Returns: 
            bool: Whether the cards can swap. 
            
        Raises:
            ValueError: No card in hand or Position Cards are incorrect.
            IndexError: Invalid index.

        Side effects:
            Modify attributes card_in_hand and position_cards.

        """
        
        if self.card_in_hand == None:
            raise ValueError("No card in hand.")
        elif self.position_cards == None or len(self.position_cards) != 10:
            raise ValueError("Position Cards are incorrect.")
        elif index < 1 or index >10:
            raise IndexError("Invalid index.")
        
        print(f"\nChecking to see if the card can be swapped at index " + 
              f"{index}.\n")

        if self.card_in_hand.number == 13 or self.card_in_hand.number == index:
            print("Cards can be swapped!\n")
            return True
        else:
            print("Cards can't be swapped.\n")
            return False
        
    def swap(self, index):
        """ Swaps card at provided index.
        
        Args:
            index (int): The index of the card in the cards attribute that the 
            card in hand is trying to swap.
            
        Side effects:
            Modifies attributes card_in_hand and position_cards.
        """
        tmp = self.position_cards[index - 1]
        tmp.reveal()
        print(f"Placing {self.card_in_hand} in the position cards. " \
            f"The card was swapped for a {tmp}.\n")
        self.position_cards[index - 1] = self.card_in_hand
        self.card_in_hand = tmp
        
class GameStage(Enum):
    """ An Enum class that represents the 4 type of game stages.
        The 4 game stages are: 1. player1_play which represents player 1 is
        currently playing; 2. player2_play which represents player 2 is
        currently playing; 3. player1_won which represents player 1 has won the
        game; 4. player2_won which represents player 2 has won the game.

    Args:
        Enum (Enum): Enum class as the parent class.

    """
    player1_play = 1
    player2_play = 2
    player1_won = 3
    player2_won = 4

class Game:
    """ A class represents a game of the Trash Card Game. The class contains two
        players, a deck of card, a list of disposed cards and a game stage enum.

    Attributes:
        game_stage (GameStage): A GameStage representing the current stage of 
            the game.
        deck (Deck): A deck of cards that represents the remaining unreveal
            cards. At the beginning of each player's round, the player can
            choose to get dealt a card from this deck or pick a card from the
            disposed cards list.
        disposed_cards (list): A list of Card objects that represents the cards
            disposed by both players. At the beginning of each player's round,
            the player can choose to pick a card from this list or get dealt a
            card from the deck.
        player1 (Player): A Player object that represents the player1.
        player2 (Player): A Player object that represents the player2.
        
    """

    def __init__(self, player1_name, player2_name):
        """ Initialize the game with the names of the 2 players. The init
            function will generate the deck with shuffling, deal 10 cards from
            the deck and create the player1 object, deal 10 cards from the deck
            and create the player2 object and randomly pick a player to start
            the game.

        Args:
            player1_name (str): The name of Player 1.
            player2_name (str): The name of Player 2.
            
        """
        self.deck = Deck()
        # position cards for player 1
        player1_position_cards = get_position_cards(self.deck)
        # position cards for player 2
        player2_position_cards = get_position_cards(self.deck)
        
        # randomly select who will start and set the game stage 
        start_player = random.randint(1,2) 
        if start_player == 1:
            self.game_stage = GameStage.player1_play
        else:
            self.game_stage = GameStage.player2_play
        
        # initialize player1 and player2 objects with the names and cards
        self.player1 = Player(player1_name, player1_position_cards)
        self.player2 = Player(player2_name, player2_position_cards)
        
        self.disposed_cards = []
        
    def play_trash(self):
        """ Facilitates game of trash between two players until one wins.

            There will be a loop starts from playing by the player of the
            gameStage. The player can choose to get dealt a card from the deck
            or pick a card from the disposed deck (the first round do not have
            this option).
            
            After getting the card in hand, there is another inner loop for the
            player to play. In the inner loop, the player can choose to either
            swap the card in hand with the card in the cards list where the
            number of the card in hand and the index of the card in the list are
            the same or disposed the card. E.g. if the card in hand has number 5
            , the player will only be allowed to swap it with the 5th card in
            the cards list. There is one exception for this rule that if the
            card in hand is a King(13), the player is allowed to swap with any
            card from the cards list. After sucessfully swapping the card,
            determines if the player has won the game or not by checking whether
            all the cards of the player are revealed. If the player has won the
            game, set the game stage to the won stage of the player (e.g.
            player1_won for player1).
            
            If the player choose to dispose the card, the card will be added to
            the disposed cards list and the player's round is over. Set the game
            stage to the play stage of the other player (e.g. if player just
            finished the round, set the game stage to player2_play) and then
            start the round of the other player.
            
            The loop will be terminated if the game stage is the won stage of
            either player. After the loop is terminated, print the winning
            message.
            
        Side effects:
            Modifies game_stage, deck, disposed_cards, player1 and player2
            attributes. Prints details of game and asks for input.
            
        """
        print("Welcome to the trash card game!\n")
        # if the game stage is the play stage, keep playing rounds between the 
        # 2 players
        while self.game_stage == GameStage.player1_play or \
            self.game_stage == GameStage.player2_play:
            
            self.take_turn()
        
        # print the final position cards of the players and the winning message
        print_position_cards(self.player1)
        print()
        print_position_cards(self.player2)
        print()
        
        if self.game_stage == GameStage.player1_won:
            print(f"{self.player1.name} won!")
        else:
            print(f"{self.player2.name} won!")
            
    def take_turn(self):
        """ Takes turn for the current player.
            
        Side effects:
            Modifies attributes of game_stage, player1, player2, disposedCard
            and/or deck attributes. 
            Prints details of game and asks for input in certain situations.
        """
        # set the current player based on the game stage
        if self.game_stage == GameStage.player1_play:
            current_player = self.player1
        else:
            current_player = self.player2
        
        # print the position cards and disposed cards pool
        print(f"{current_player.name}'s round: ")
        print()
        print_position_cards(current_player)
        print("Disposed cards:")
        print_cards_list(self.disposed_cards)
        
        # get the card in hand for the current player
        self.get_card_in_hand(current_player)
        
        print(f"Card in hand: {current_player.card_in_hand}\n")
        
        # current player takes actions with the card in hand
        self.play_card(current_player)
        
        # update the game stage if it is either player1_play or player2_play
        # stage
        if self.game_stage == GameStage.player1_play:
            self.game_stage = GameStage.player2_play
        elif self.game_stage == GameStage.player2_play:
            self.game_stage = GameStage.player1_play
        
        print()
        
    def get_card_in_hand(self, current_player):
        """ Get the card in hand for the current player. The card in hand can
            be dealt from the deck or picked from the disposed cards pool.        

        Args:
            current_player (Player): the current player of the round.
        
        Side effects:
            Modifies attributes of player1, player2, disposedCard and/or deck 
            attributes. 
            Prints details of game and asks for input in certain situations.
        """
        # ask player until the player has a card in hand
        while current_player.card_in_hand == None:
            decision = input("Would you like to draw a card(1) or get a card " +
                    "from the disposed card pool(2)? ")
            
            if decision == "1": # if user choose to get the card from deck
                current_player.card_in_hand = self.deck.deal()
            elif decision == "2": # if user choose to get the card from the
                # disposed cards pool
                
                if (len(self.disposed_cards) == 0): # if there is no card in the
                    # disposed cards pool
                    print("No card in the disposed pool.\n")
                else:
                    index = None
                    
                    # ask the player to pick an index for the card in the 
                    # disposed cards pool until it is valid
                    while index == None:
                        decision = input("\nWhich card would you want to " +
                            "pick from the disposed card pool? Please " +
                            "input the index: ")
                        if int(decision) <= len(self.disposed_cards) \
                            and int(decision) > 0:
                            index = int(decision)
                        else:
                            print("\nIncorrect input. Please re-enter.")
                    
                    current_player.card_in_hand = self.disposed_cards.pop(index\
                        - 1)
            else:
                print("\nIncorrect selection, please re-enter your choice.")
            
            print()

    def play_card(self, current_player):
        """ Current player plays the card in hand. The player can choose to 
            either swap it with a position card or dispose the card.

        Args:
            current_player (Player): the current player of the round.
        
        Side effects:
            Modifies attributes of player1, player2, disposedCard and/or deck 
            attributes. 
            Prints details of game and asks for input in certain situations.
        """
        # ask the player what the player wants to do with the card in hand
        action = input("Would you want to swap your card with a position " +
            "card(1) or dispose your card(2)? ")
        
        # while the action is not dispose the card, keep the loop running
        while action != "2":
            
            if action == "1": # if the player choose to swap the card in hand
                # with a position card
                position = int(input("\nWhere would you like to place your "
                    + "card [1-10]? "))
                
                if position > 0 and position <= 10: # if the index is valid
                    if current_player.check_swap(position): # if the cards can
                        # be swapped
                        current_player.swap(position)
                        if hasWon(current_player): # if the current player has 
                            # won, set the game stage to win stage and break the
                            # loop
                            if self.game_stage == GameStage.player1_play:
                                self.game_stage = GameStage.player1_won
                            elif self.game_stage == GameStage.player2_play:
                                self.game_stage = GameStage.player2_won
                            break
                    else: # if the cards can not be swapped
                        print("Unable to place the card. Plase try other " +
                            "action.\n")
                else: # if the index is invalid
                    print("\nIncorrect index input.\n")
                
                print_position_cards(current_player)
                print(f"Card in hand: {current_player.card_in_hand}")
            else: # if the selection is not 1 or 2
                print("\nIncorrect selection, please re-enter your choice.")
                
            print()
            # ask the player again what the player wants to do with the card in 
            # hand
            action = input("Would you want to swap your card with a " +
                "position card(1) or dispose your card(2)? ")
        
        # current player finishes the round
        # dispose the current player's card in hand to the disposed card pool
        self.dispose_card(current_player)
        
    def dispose_card(self, current_player):
        """ dispose the card in hand from the current player to the disposed 
            cards pool.

        Args:
            current_player (Player): the current player playing the round.
        
        Side effects:
            Modifies attributes of player1, player2 and/or disposedCard.
        """
        self.disposed_cards.append(current_player.card_in_hand)
        current_player.card_in_hand = None
            
def get_position_cards(deck):
    """ get position cards for each player each round.
    """
    position_cards = deck.deal(10)
    return position_cards

def print_position_cards(player):
    """ print the player's position cards
    
    args:
        player (Player): a player 
    """
    
    print(f"{player.name}'s position cards:")
    pos = 1
    for card in player.position_cards:
        print(f"{pos:<2}: {card}")
        pos += 1
    print()

def print_cards_list(cards):
    """ Display a list of cards 

    Args:
        cards (list): list of cards
    """
    for i, card in enumerate(cards):
        if card.revealed:
            print(f"{i + 1}: {card}")
    print()

def hasWon(player):
    """ Determines if a player has won the game. Returns True if all the cards
        of the player are revealed and False otherwise.

    Args:
        player (Player): a Player object for checking the winning status.

    Returns:
        bool: boolean of whether the player has won the agme or not.

    """
    return all(card.revealed for card in player.position_cards)

def main(player1_name, player2_name):
    """ Initialize the Game with the player 1 name and player 2 name and play
        the game.

    Args:
        player1_name (str): the name of player 1
        player2_name (str): the path of player 2

    """
    game = Game(player1_name, player2_name)
    game.play_trash()

def parse_args(arglist):
    """ Parse command-line arguments.

    Expect two mandatory arguments (two string values represent player 1 and
        player 2 names.

    Args:
        arglist (list of str): arguments from the command line.

    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("player1_name", help="string represents the"
                        " name of player 1.")
    parser.add_argument("player2_name", help="string represents the"
                        " name of player 2.")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player1_name, args.player2_name)
