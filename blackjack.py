import random
import sqlite3

points = {'A': 1, 'J': 10, 'Q': 10, 'K':10}
points.update({n: n for n in range(2, 11)})

def hand_score(hand):
    """Total score for a hand."""
    total = sum([points[card] for card in hand])
    if total <= 11 and 'A' in hand:
        return total + 10
    return total

db = sqlite3.Connection('cards.db')
sql = db.execute
sql('DROP TABLE IF EXISTS cards')
sql('CREATE TABLE cards(card, place);')

def play(card, place):
    """Play a card so that the player can see it."""
    sql('INSERT INTO cards VALUES (?, ?)', (card, place))
    db.commit()

def score(who):
    """Compute the hand score for the player or dealer."""
    cards = sql('SELECT * from cards where place = ?;', [who])
    return hand_score([card for card, place in cards.fetchall()])

def bust(who):
    """Check if the player or dealer went bust."""
    return score(who) > 21

player, dealer = "Player", "Dealer"

def play_hand(deck):
    """Play a hand of Blackjack."""
    play(deck.pop(), player)
    play(deck.pop(), dealer)
    play(deck.pop(), player)
    hidden = deck.pop()
    print("Dealer's Cards")
    dealer_cards = sql('SELECT card FROM cards WHERE place = "Dealer";').fetchall()
    print([card[0] for card in dealer_cards])
    print("Player's Cards")
    player_cards = sql('SELECT card FROM cards WHERE place = "Player";').fetchall()
    print([card[0] for card in player_cards])
    while 'y' in input("Hit? ").lower():
        play(deck.pop(), player)
        player_cards = sql('SELECT card FROM cards WHERE place = "Player";').fetchall()
        print([card[0] for card in player_cards])
        if bust(player):
            print(player, "went bust!")
            print("Dealer wins")
            return
    print("Back to dealer's turn")
    play(hidden, dealer)
    print("Dealer's Cards")
    dealer_cards = sql('SELECT card FROM cards WHERE place = "Dealer";').fetchall()
    print([card[0] for card in dealer_cards])

    while score(dealer) < 17:      
        play(deck.pop(), dealer)
        dealer_cards = sql('SELECT card FROM cards WHERE place = "Dealer";').fetchall()
        print([card[0] for card in dealer_cards]) 
        if bust(dealer):
            print(dealer, "went bust!")
            print("Player wins")
            return

    print(player, score(player), "and", dealer, score(dealer))
    if score(player) < score(dealer):
        print("Dealer wins")
    elif score(player) > score(dealer):
        print("Player wins")
    else:
        print("Tie")

playing = True
deck = list(points.keys()) * 4
random.shuffle(deck)
while playing:
    print('\nDealing...')
    play_hand(deck)
    sql('UPDATE cards SET place="Discard";')
    if 'n' in input("Keep playing? ").lower():
        playing = False
    if len(deck) < 10:
        print("Reshuffling")
        deck = list(points.keys()) * 4
        random.shuffle(deck)
        sql("DELETE FROM cards;")