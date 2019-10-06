# Blackjack Design Document

### What is this?
This is a terminal based blackjack game, built-in Python. It currently supports only single player with an automated dealer.

### To play
Simply download the repository and run the Python file.

From terminal:

`git clone https://github.com/ManavR123/blackjack.git` 

`cd blackjack`

`python blackjack.py` (or `python3 blackjack.py` for Mac users)

### System Architecture
The code layout is purely functional. No classes! There was no need for multiple layers of abstraction due to lightweight nature of the game. So, I kept the code to just a simple set of functions that still allowed for modularity.

The main data structures used are dictionaries. Dictionaries were very useful due to their constant access time.

The `points` dictionary allowed me to update a player's score elegantly as oppossed to writing a function with several different value checks for a card.

The `playerScore` dictionary allowed me to easily to keeping a running tally on a player's score instead of constantly re-evaluating a player's hand through a linear pass over their cards.

The `playerHasAce` dictionary allowed me to avoid a linear pass over the player's hand every time I needed to evaluate their score.

The `players` dictionary stored the hands for the player and the dealer. The reason I opted in for this instead of simply having two arrays, one for the dealer and one for the player, is two-fold. One, it allowed my code to be more concise since I didn't have to do explicit checks on who's hand I needed to update. Second, in the event I want to add support for more players, this infrastructure is well-catered to do so. I would simply just need to cycle through the number of players in the `play` function. The dictionary I currently have works to effectively store all players hands for any given number of players. However, until I implement this added functionality, I made use of the infrastructure by having variables denoting keys for just the Dealer and the Player.

### Why Python?
I wanted to keep my code simple and readable and Python was well-suited for this job. I knew coming into development that this program wouldn't be overwhelmingly complex, so I wanted to take advantage of Python's scripting capabilities to make this program lightweight.