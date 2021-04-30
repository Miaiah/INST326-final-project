""" Final project check in 1

"""
from argparse import ArgumentParser
import random
from enum import Enum

import sys

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
            return f"{self.number} {self.suit}"
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
        self.discards = []
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

            dealedCards = []
            for i in range(count):
                dealedCards.append(self.cards.pop())
            return dealedCards

class Player:
    """ A class of player information with name, the list of the cards of the
        player and the card in the hand of the player.

    Attributes:
        name (str): name of player.
        positionCards (list): A list of Card objects representing the cards
            a player has for the game. Initially, the player has 10 unrevealed
            cards.
        cardInHand (Card): a card the player is dealt from the deck or from the
            disposed pool for making different decisions including swapping with
            one of the card frmo the cards of the player and disposing the card
            which will append the card to the disposed pool.

    """

    def __init__(self, name, positionCards, cardInHand = None):
        """ Initialize the player with a name, list of the cards of the player
            and an optional card in hand.

        Args:
            name (name): The name of the player.
            positionCards (list): A list of 10 unrevealed Card objects
                representing the cards a player initially has for the game.
            cardInHand (Card, optional): A Card object representing the card the
                player has in hand to play the game. Defaults to None.

        """
        self.name = name
        self.positionCards = positionCards
        self.cardInHand = cardInHand
        self.table = []
        self.table = get_table(10)

    def draw_card(self):
        self.cardInHand = card.cards.pop(0)
        self.cardInHand.reveal()
        print(f"You have drew a card : {self.cardInHand}")
        print("")

    def swap(self, index):
        """ Try to swap a card in hand with a position card. If the cards can be
        swapped, retuen True. Otherwise return False.

        Args:
            index (int): The index of the card in the cards attribute that the
            card in hand is trying to swap.

        Returns:
            bool: Whether the swap is successful.

        Raises:
            ValueError: No card in hand or Position Cards are incorrect.
            IndexError: Invalid index.

        Side effects:
            Modify attributes cardInHand and positionCards.

        """

        if self.cardInHand == None:
            raise ValueError("No card in hand.")
        elif self.positionCards == None or len(self.positionCards) != 10:
            raise ValueError("Position Cards are incorrect.")
        elif index < 1 or index >10:
            raise IndexError("Invalid index.")


        if self.cardInHand.number == 13 or self.cardInHand.number == index:
            tmp = self.positionCards[index - 1]
            self.positionCards[index - 1] = self.cardInHand
            self.cardInHand = tmp
            self.cardInHand.reveal()
            return True
        else:
            return False


class GameStage(Enum):
    """ An Enum class that represents the 4 type of game stages.
        The 4 game stages are: 1. Player1Stage which represents player 1 is
        currently playing; 2. Player2Stage which represents player 2 is
        currently playing; 3. Player1Won which represents player 1 has won the
        game; 4. Player2Won which represents player 2 has won the game.

    Args:
        Enum (Enum): Enum class as the parent class.

    """
    Player1Stage = 1
    Player2Stage = 2
    Player1Won = 3
    Player2Won = 4

class Game:
    """ A class represents a game of the Trash Card Game. The class contains two
        players, a deck of card, a list of disposed cards and a game stage enum.

    Attributes:
        gameStage (GameStage): A GameStage representing the current stage of the
            game. Game stages include Player1Stage
        deck (Deck): A deck of cards that represents the remaining unreveal
            cards. At the beginning of each player's round, the player can
            choose to get dealt a card from this deck or pick a card from the
            disposed cards list.
        disposedCards (list): A list of Card objects that represents the cards
            disposed by both players. At the beginning of each player's round,
            the player can choose to pick a card from this list or get dealt a
            card from the deck.
        player1 (Player): A Player object that represents the player1.
        player2 (Player): A Player object that represents the player2.

    """

    def __init__(self, player1Name, player2Name):
        """ Initialize the game with the names of the 2 players. The init
            function will generate the deck with shuffling, deal 10 cards from
            the deck and create the player1 object, deal 10 cards from the deck
            and create the player2 object and randomly pick a player to start
            the game.

        Args:
            player1Name (str): The name of Player 1.
            player2Name (str): The name of Player 2.

        """
        

    def playTrash(self):
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
            Player1Won for player1).

            If the player choose to dispose the card, the card will be added to
            the disposed cards list and the player's round is over. Set the game
            stage to the play stage of the other player (e.g. if player just
            finished the round, set the game stage to Player2Stage) and then
            start the round of the other player.

            The loop will be terminated if the game stage is the won stage of
            either player. After the loop is terminated, print the winning
            message.

        Side effects:
            Modifies gameStage, deck, disposedCards, player1 and player2
            attributes. Prints details of game and asks for input.

        """
def get_table(cards_table):
    """get table for each player each round.
    """
    table = []
    for i in range(cards_table):
        card_draw = card.cards.pop(0)
        table.append(card_draw)
    return table

def print_table(player):
    """ print the player's table
    
    args:
        player (Player): a player 
    """
    
    print(f"{player.name}'s position cards:")
    pos = 1
    for card in player.table:
        print(f"{pos:<2}: {card}")
        pos += 1
    print()

def place_card(player, position):
    card_changed = player.table.pop(position)
    player.table.insert(position, player.cardInHand) #place card
    player.table[position].revealed = True #reveal card
    player.cardInHand = card_changed
    player.cardInHand.reveal()
    print("You have placed the card.")
    print("")
    print_table(player)
    print(f"Now your card in hand is: {player.cardInHand}")

def play(player):
    out = 0
    while out < 1:
        if player.cardInHand.number > 11: #can't do anything. pass term
            while True:
                decision = input("Do you want to discard the card? Y/N: ")
                if decision == "Y":
                    out = 1
                    break
                elif decision == "N":
                    print("You can only discard the card.")
                else:
                    print("Invalid input.")
        elif player.cardInHand.number == 11: #replace card to anywhere
            while True:
                position = int(input("Choose a position between 1 - 10: ")) 
                #get a postion
                if position > 10 or position < 1:
                    print("Invalid position.")
                else:
                    break
            position -= 1
            place_card(player, position)
        else: #card number between 1 - 10
            while True:
                decision = input("Do you want to discard the card? Y/N: ")
                print("")
                if player.cardInHand.number == 11:
                    break
                elif decision == "N":
                    while True:
                        pos_choose = int(input("Where do you want to place " +
                                               "your card? ")) - 1
                        position = player.cardInHand.number - 1
                        if pos_choose != position:
                            print("Invalid position. Please try again.")
                        else:
                            if not player.table[position].revealed:
                                place_card(player, position)
                                break
                            elif player.table[position].revealed and \
                                player.table[position].number == position + 1:
                                print("You can not place the card on this " + 
                                      "position. ")
                                break
                            elif player.table[position].revealed and \
                                player.table[position].number == 11:
                                place_card(player, position)
                                break
                elif decision == "Y":
                    out = 1
                    break
                else:
                    print("Invalid answer. Please try again.")

def count_deck(card):
    """count the number of cards in the deck
    """
    count = 0
    for i in card.cards:
        count += 1
    print("The deck has ", count, " cards now.")
    print("")

def discard(player):
    """help the user discard the card
    """
    player.cardInHand.revealed = True
    card.discards.append(player.cardInHand)
    player.cardInHand = None

def fill_deck(card):
    """fill the deck from discard deck"""
    one_card = card.discards.pop() #at least one card in discards deck
    for item in card.discards:
        item.revealed = False
        card.cards.append(item)
    card.discards.append(one_card)

def check_deck(card):
    """check that is the deck empty, if it is, we fill the deck
    """
    count = 0
    for i in card.cards:
        count += 1
    if count > 0: #check is the deck empty
        pass
    else:   #If it is empty, fill it
        fill_deck(card)

def hasCard(player, card):
    """ Determines if player already has the dealt/chosen card.

    Args:
        player (Player): a Player object.
        card (Player): a card object the player was dealt.

    Returns:
        bool: boolean of whether player has card or not. True if they do.

    """

def hasWon(player):
    """ Determines if a player has won the game. Returns True if all the cards
        of the player are revealed and False otherwise.

    Args:
        player (Player): a Player object for checking the winning status.

    Returns:
        bool: boolean of whether the player has won the agme or not.

    """

def main(player1Name, player2Name):
    """ Initialize the Game with the player 1 name and player 2 name and play
        the game.

    Args:
        player1Name (str): the name of player 1
        player2Name (str): the path of player 2

    """
    card = Deck()
    #player1 round
    player1 = Player(player1Name) #have a table for player1 now
    print_table(player1)
    check_deck(card) #check is the deck empty, if it is, fill the card deck
    player1.draw_card() #draw a card
    count_deck(card)
    play(player1) #play
    discard(player1) #discard the card in your hand



    #player2 round
    player2 = Player(player2Name) #have a table for player2 now
    print_table(player2)
    check_deck(card)
    player2.draw_card()
    count_deck(card)
    play(player2)
    discard(player2)

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
    parser.add_argument("player1Name", help="string represents the"
                        " name of player 1.")
    parser.add_argument("player2Name", help="string represents the"
                        " name of player 2.")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player1Name, args.player2Name)
