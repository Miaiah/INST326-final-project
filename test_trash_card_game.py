from pytest import fixture
import trash_card_game as trash

@fixture
def deck1():
    return trash.Deck()

def test_deal(deck1):
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

def test_deck():
    """Does build_deck generate correct number of cards?"""
    card_deck = trash.Deck()
    card_number = 0
    for item in card_deck.cards:
        card_number += 1
    assert card_number ==  52

