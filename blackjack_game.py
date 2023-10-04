import random

# Define the deck of cards with values 2 to 10 with 11 being the ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """
    Returns a random card from the deck of cards.
    """
    random_card = random.choice(cards)
    return random_card

def calculate_score(card_list):
    """
    Takes a list of cards and returns the sum of the card values.
    """
    card_sum = sum(card_list)
    if card_sum == 21 and len(card_list) == 2:
        card_sum = blackjack

    if 11 in card_list and card_sum > 21:
        card_list.remove(11)
        card_list.append(1)
        card_sum = card_list

    return card_sum

# Calculate the sum of a list of cards, handling special cases for blackjack and Ace.
blackjack = 0

#Compare the final scores and determine the winner.
def compare(player_score, computer_score):
    if player_score == computer_score:
        return f"Computer has {computer_score} and Player has {player_score}. Draw Game."
    elif computer_score == blackjack:
        return f"Computer has Blackjack. Computer Wins. Player Loses"
    elif player_score == blackjack:
        return "Player has Blackjack. Player Wins. Computer Loses"
    elif computer_score > 21:
        return f"Computer Bust with a score of {computer_score}. Player Wins with a score of {player_score}"
    elif player_score > 21:
        return f"Player Bust with a score of {player_score}. Computer Wins with a score of {computer_score}"
    elif computer_score > player_score:
        return f"Computer Wins with a score of {computer_score}. Player had {player_score}"
    else:
        return f"Player Wins with a score of {player_score}. Computer had {computer_score}"


def new_game():
    # Deal 2 cards each for the user and the computer.
    user_cards = []
    computer_cards = []
    for card_dealt in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())



    # Check for game-ending conditions and prompt the user to draw another card.
    game_over = False

    while not game_over:
        player_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"The computer's first card is {computer_cards[0]}")
        print(f"The player's cards are {user_cards}. Player score is {player_score}.")

        if player_score == blackjack or computer_score == blackjack or player_score > 21:
            game_over = True
        else:
            play_again = input("Would you like to draw another card? Y or N?: ").lower()

            if play_again == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Let the computer play until it has a score less than 17.
    while computer_score != blackjack and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(compare(player_score, computer_score))

# Ask the user if they want to restart the game.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  new_game()

