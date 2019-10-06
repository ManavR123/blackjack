import random

def play_card(card, who):
    """Play a card so that the player can see it."""
    playerHand = players.get(who)
    # If current player hasn't gotten a card yet, create a new hand for them
    if playerHand == None:
        playerHand = [card]
        playerScore[who] = points[card]
        players[who] = playerHand
    else:
        playerScore[who] = playerScore[who] + points[card]
        playerHand.append(card)
    # Keep track of players who have Aces
    if card == 'A':
        playerHasAce[who] = True

def score(who):
    """Compute the hand score for the player or dealer."""
    score = playerScore[who]
    # Increment score if player has an Ace
    if score <= 11 and playerHasAce.get(who):
        score += 10
    return score

def bust(who):
    """Check if the player or dealer went bust."""
    return score(who) > 21

def play(deck):
    """Play a hand of Blackjack."""
    play_card(deck.pop(), DEALER)
    play_card(deck.pop(), PLAYER)
    # We will hide 2nd card for dealer for now
    hidden = deck.pop()
    play_card(deck.pop(), PLAYER)
    print("Dealer's Cards")
    print([card for card in players[DEALER]])
    print("Player's Cards")
    print([card for card in players[PLAYER]])
    while 'y' in input("Hit? (y/n) ").lower():
        play_card(deck.pop(), PLAYER)
        print([card for card in players[PLAYER]])
        if bust(PLAYER):
            print("Player went bust!")
            print("Dealer wins")
            return

    print("Back to dealer's turn")
    play_card(hidden, DEALER)
    print("Dealer's Cards")
    print([card for card in players[DEALER]])

    # Dealer must have at least 17
    while score(DEALER) < 17:
        play_card(deck.pop(), DEALER)
        print([card for card in players[DEALER]])
        if bust(DEALER):
            print("Dealer went bust!")
            print("Player wins")
            return

    print("Player scored", score(PLAYER), "and Dealer scored", score(DEALER))
    if score(PLAYER) < score(DEALER):
        print("Dealer wins")
    elif score(PLAYER) > score(DEALER):
        print("Player wins")
    else:
        print("Tie")

# Set point values for all cards
points = {'A': 1, 'J': 10, 'Q': 10, 'K':10}
points.update({n: n for n in range(2, 11)})

# Create playing deck with 6 actual decks
deck = list(points.keys()) * 6
# Shuffle deck
random.shuffle(deck)

# Denote keys that correspond to dealer and player
DEALER = 0
PLAYER = 1

# Begin play cycle
playing = True
while playing:
    # Create dictionaries to store all hands
    players = {}
    playerScore = {}
    playerHasAce = {}

    print("\nDealing...")
    play(deck)
    if 'n' in input("Keep playing? (y/n) ").lower():
        playing = False

    # If deck becomes small reshuffle so we don't run out of cars
    if len(deck) < 10:
        print("Reshuffling")
        deck = list(points.keys()) * 6
        random.shuffle(deck)