# INST326-final-project
### Trash (Garbage) card game
### Rules: https://bicyclecards.com/how-to-play/trash/#filter=.2 
### Video: https://www.youtube.com/watch?v=tKWvR-43Ukc 

For the final project , we are going to implement The Trash (Garbage) card game which will be played by two players, using one standard deck of 52 cards. This idea is borrowed from https://bicyclecards.com/how-to-play/trash/#filter=.2. 

The objective of the game is to be the first player that collects a complete set of 10 cards, which is Ace through 10 in sequence. Each player will start with 10 cards, faced down, from left to right in an increasing order position (which the final goal would be Ace - 10). The remaining of the deck of cards are all face down. 

Each round, a player can either draw a card from the deck or pick a card from the discarded pile of cards. Depending on the card the player picks, if it is J or Q, the round is over since there is no J or Q position in the 10 card list of the player and the player will need to discard the card and end the round. If the card is Ace - 10, the player can choose to replace the card with the corresponding position card (e.g. Ace for position 1 card) if that card in the position is still faced down. If the card is K, a wild card, the player can choose to replace it with any position position card. Once the card is replaced, the player will have a new card in hand. The player can keep playing the round until the player is unable to make any more changes (replacing with the card list). 
