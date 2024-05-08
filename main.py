import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_score(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. you lose!"
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "You won with a blackjack"
    elif computer_score == 0:
        return "Opponent win with a blacjack"
    elif user_score > 21:
        return "You went over, You lose!"
    elif computer_score > 21:
        return "opponent went over, You Win!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose."

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    print(logo)
    for starting_cards in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)
        print(f"Your cards are {user_cards}, your score is {user_score}")
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to gte another card, type 'n' to pass")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))



while input("Do you want to play blackjack? type 'y' for yes or 'n' for no: "):
    play_game()