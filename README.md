# INST326-final-project
### Trash (Garbage) card game
### Rules: https://bicyclecards.com/how-to-play/trash/#filter=.2 
### Video: https://www.youtube.com/watch?v=tKWvR-43Ukc 


### trash_card_game.py
For the final project , we are going to implement The Trash (Garbage) card game which will be played by two players, using one standard deck of 52 cards. This idea is borrowed from https://bicyclecards.com/how-to-play/trash/#filter=.2. 

The objective of the game is to be the first player that collects a complete set of 10 cards, which is Ace through 10 in sequence. Each player will start with 10 cards, faced down, from left to right in an increasing order position (which the final goal would be Ace - 10). The remaining of the deck of cards are all face down. 

Each round, a player can either draw a card from the deck or pick a card from the discarded pile of cards. Depending on the card the player picks, if it is J or Q, the round is over since there is no J or Q position in the 10 card list of the player and the player will need to discard the card and end the round. If the card is Ace - 10, the player can choose to replace the card with the corresponding position card (e.g. Ace for position 1 card) if that card in the position is still faced down. If the card is K, a wild card, the player can choose to replace it with any position position card. Once the card is replaced, the player will have a new card in hand. The player can keep playing the round until the player is unable to make any more changes (replacing with the card list). 


### test_trash_card_game.py
[An explanation of the purpose of test_trash_card_game.py]


### How to run program from the command line:
python3 trash_card_game.py player1name player2name  (on macOS) 

python3 trash_card_game.py player1name player2name  (on Windows) 


### How to use the program to interpret the output of the program: 
First, the game will start off randomly pick one player to be the first player and ask “Would you like to draw a card(1) or get a card from the disposed card pool(2)?” The first player will have to enter “1” since there is no card in the disposed card pool yet.

After the player get the first card in hand, the game will ask the player “Would you want to swap your card with a position card(1) or dispose your card(2)?” Based on the card in hand, the player will make the choice by entering “1” or “2”.

If the player chooses “1” which is to swap card with position card, the game will ask “Where would you like to place your card [1-10]?” The player should enter the corresponding index of the position card that the player wants to swap, which should have the same number as the card in hand(unless the card in hand is a king). This swapping process will continue until the player is not able to swap card with position card.

If the player chooses “2” which is to dispose the card in hand, then the player’s round ends and the card will be added to the disposed card pool.
