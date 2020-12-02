import random
from database import logo

game_on = True

while game_on:
    # Logo and welcome message 
    print(logo)
    print("Welcome to Python BlackJack!\n")

    def compare(u_score, c_score):
        if u_score == c_score:
            return "It's a draw"
        elif c_score == 0 or c_score > u_score and c_score <= 21:
            return "The computer wins"
        elif u_score == 0 or u_score > c_score and u_score <= 21:
            return "You win"
        elif u_score > 21:
            return "The computer wins"
        elif c_score > 21:
            return "You win"


    def calculate_score(cards_list):
        if len(cards_list) == 2 and sum(cards_list) == 21:
            return 0

        if 11 in cards_list and sum(cards_list) > 21:
            cards_list.remove(11)
            cards_list.append(1)

        return sum(cards_list)

    # Return a random card
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    # User and computer's hands
    user_cards = []
    computer_cards = []

    # Add two random cards to user's and computer's hands
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"Your hand: {user_cards}\n")
    print(f"Computer hand: [{computer_cards[0]}]\n")

    # sum up user's and computer's hands
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # print result
    print(f"Your score is: {user_score}\n")

    is_game_over = False
    while is_game_over == False:
        if computer_score == 0 or user_score == 0 or user_score > 21 or computer_score > 21:
            is_game_over = True
        else:
            user_choice = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
            if user_choice == "y":
                # deal another card
                user_cards.append(deal_card())
                # recalculate the score
                user_score = calculate_score(user_cards)
                # print results
                print(f"Your hand: {user_cards}\n")
                print(f"Your score is: {user_score}\n")
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
    # deal another card
        computer_cards.append(deal_card())
        # recalculate the score
        computer_score = calculate_score(computer_cards)
        # print results
        print(f"Computer hand: {computer_cards}\n")
    else:
        is_game_over = True

    game_result = compare(user_score, computer_score)

    print(game_result)

    restart_game = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if restart_game == "n":
        game_on = False

