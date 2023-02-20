import random

# Define the card values and names
card_values = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

# Define a class to represent a deck of cards
class Deck:
    def __init__(self):
        self.cards = list(card_values.keys()) * 4
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()

# Define a class to represent a hand of cards
class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def get_value(self):
        value = sum([card_values[card] for card in self.cards])
        aces = [card for card in self.cards if card == "Ace"]
        for ace in aces:
            if value > 21:
                value -= 10
        return value

# Define a function to ask the player for their bet amount
def get_bet(chips):
    while True:
        try:
            bet = int(input(f"How much would you like to bet? (You have {chips} chips) "))
        except ValueError:
            print("Please enter a valid integer.")
        else:
            if bet < 1:
                print("Please enter a positive integer.")
            elif bet > chips:
                print("You don't have enough chips for that bet.")
            else:
                return bet

# Define a function to ask the player whether to hit or stand
def get_action():
    while True:
        action = input("Do you want to hit or stand? ")
        if action.lower() in ["hit", "stand"]:
            return action.lower()
        else:
            print("Please enter either 'hit' or 'stand'.")

# Define a function to ask the player whether to play again
def play_again():
    while True:
        again = input("Do you want to play again? (y/n) ")
        if again.lower() in ["y", "n"]:
            return again.lower()
        else:
            print("Please enter either 'y' or 'n'.")

# Start the game
print("Welcome to Blackjack!")

while True:
    # Create the deck and hands
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    
    # Deal the initial cards
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card(hidden=True))
    
    # Ask for the bet amount
    chips = 100
    bet = get_bet(chips)
    
    # Show the hands
    print(f"Dealer's hand: {dealer_hand.cards[0]}, hidden")
    print(f"Your hand: {', '.join(player_hand.cards)} ({player_hand.get_value()})")
    
    # Player's turn
    while True:
        action = get_action()
        if action == "hit":
            player_hand.add_card(deck.deal_card())
            print(f"Your hand: {', '.join(player_hand.cards)} ({player_hand.get_value()})")
            if player_hand.get_value() > 21:
                print("Bust! You lose.")
                chips -= bet
                break
        else:
            break
    
    # Dealer's turn
    if player_hand.get_value() <= 21:
        dealer_hand.cards[0] = dealer_hand.cards[1]
        print(f"Dealer's hand: {', '.join(dealer_hand.cards)} ({dealer_hand.get_value()})")
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            print(f"Dealer hits: {dealer_hand.cards[-1]}")
            print(f"Dealer's hand: {', '.join(dealer_hand.cards)} ({dealer_hand.get_value()})")
        if dealer_hand.get_value() > 21:
            print("Dealer busts! You win.")
            chips += bet
        elif dealer_hand.get_value() > player_hand.get_value():
            print("You lose.")
            chips -= bet
        elif dealer_hand.get_value() < player_hand.get_value():
            print("You win!")
            chips += bet
        else:
            print("Push.")
    
    # Show the final hands
    print(f"Dealer's hand: {', '.join(dealer_hand.cards)} ({dealer_hand.get_value()})")
    print(f"Your hand: {', '.join(player_hand.cards)} ({player_hand.get_value()})")
    print(f"You have {chips} chips.")
    
    # Ask if the player wants to play again
    if chips < 1:
        print("You're out of chips! Game over.")
        break
    else:
        again = play_again()
        if again == "n":
            break
