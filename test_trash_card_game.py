from pytest import fixture
import trash_card_game as trash

@fixture
def deck1():
    """ Create a Deck object for testing.

    Returns:
        Deck: a new initialized Deck object for testing
    """
    return trash.Deck()

def test_deal(deck1):
    """ Test the deal() method from the Deck class with no parameter and a
        integer 10 as parameter.

    Args:
        deck1 (Deck): The Deck object for testing.

    """

    """Does deal() deals the correct number of card and the right card?"""
    """Deal 1 card"""
    length = len(deck1.cards)
    last_card = deck1.cards[-1]
    dealed_card = deck1.deal()
    assert last_card.number == dealed_card.number
    assert last_card.suit == dealed_card.suit
    assert dealed_card.revealed
    assert len(deck1.cards) == length - 1

    """Deal 10 cards"""
    length = len(deck1.cards)
    dealed_cards = deck1.deal(10)
    assert len(dealed_cards) == 10
    assert len(deck1.cards) == length - 10
    
def test_swap(capsys):
    """Does check_swap and swap functions output correctly?"""
    test_deck = trash.Deck()
    player_position_cards = trash.get_position_cards(test_deck)
    player1 = trash.Player("Player", player_position_cards, trash.Card(trash.Suit.Spade, 7, True))
    player_card = player1.position_cards[6]
    
    player1.check_swap(7)
    player1.swap(7)
    
    
    outerr = capsys.readouterr()
    out = outerr.out
    assert out == f"\nChecking to see if the card can be swapped at index 7.\n\n" \
                    f"Cards can be swapped!\n\n" \
                    f"Placing 7 Spade in the position cards. " \
                    f"The card was swapped for a {player_card}.\n\n"
    

def test_deck():
    """Does build_deck generate correct number of cards?"""
    card_deck = trash.Deck()
    card_number = 0
    for item in card_deck.cards:
        card_number += 1
    assert card_number ==  52

