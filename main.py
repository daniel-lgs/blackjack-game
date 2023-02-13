from art import logo
from replit import clear
import random


blackjack = 21
end_game = False
players = [
    {"name": "user", "cards": [], "score": 0},
    {"name": "dealer", "cards": [], "score": 0}
]


def greeting():
    print(logo)
    input("Welcome to the blackjack game! Type enter to start...")
    clear()


def draw_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def score(user_or_dealer):
    if user_or_dealer == "user":
        return sum(players[0]["cards"])
    elif user_or_dealer == "dealer":
        return sum(players[1]["cards"])
    

def print_score_board(parcial_or_complete):
    user_cards = players[0]["cards"]
    user_score = score("user")
    dealer_cards = players[1]["cards"]
    dealer_score = score("dealer")
    print(f"Your cards: {user_cards} | Your score: {user_score}")
    if parcial_or_complete == "parcial":
        print(f"Dealer's first card: {dealer_cards[0]}")
    elif parcial_or_complete == "complete":
        print(f"Dealer's cards: {dealer_cards} | Dealer's score: {dealer_score}")


greeting()


while not end_game:
    # Start the game with two random cards each user
    print(logo)
    for player in players:
        for step in range(2):
            player["cards"].append(draw_card())
    print_score_board("parcial")

    # Time for decision and user's particular rules
    draw_or_pass = "y"
    while draw_or_pass == "y":
        draw_or_pass = input("    Type 'y' to draw a card or 'n' to pass: ").lower()
        if draw_or_pass == "y":
            players[0]["cards"].append(draw_card())
            while score("user") > blackjack and 11 in players[0]["cards"]:
                for i in range(0, len(players[0]["cards"])):
                    if players[0]["cards"][i] == 11:
                        players[0]["cards"][i] = 1
                        break
            if score("user") > blackjack:
                break
            print_score_board("parcial")
        elif draw_or_pass == "n":
            break
        else:
            draw_or_pass = "y"

    # Here the winner's decision begins
    if score("user") > blackjack:
        print_score_board("complete")
        print("    You lost 😢. The dealer won.")
    else:
        # Time for decision and dealer's particular rules
        while score("dealer") < 17:
            players[1]["cards"].append(draw_card())

        # The winner's decision continues...
        if score("dealer") > blackjack:
            print_score_board("complete")
            print("    Congratulations! You won ❤️")
        else:
            if score("user") == score("dealer"):
                print_score_board("complete")
                print("    Was a draw ⚔️")
            elif score("user") > score("dealer"):
                print_score_board("complete")
                print("    Congratulations! You won ❤️")
            else:
                print_score_board("complete")
                print("    You lost 😢. The dealer won.")

    # Play again or not
    play_again = ""
    while play_again != "y" and play_again != "n":
        play_again = input("Do you want play again (y/n)? ").lower()
    if play_again == "y":
        players[0]["cards"].clear()
        players[1]["cards"].clear()
        clear()
    else:
        end_game = True
