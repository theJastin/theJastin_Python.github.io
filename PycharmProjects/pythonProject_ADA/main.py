import random

def choose_rps():
    return random.choice(["rock", "paper", "scissors"])
    # r = random.randint(0,2)
    # if r == 0:
    #     return "rock"
    # elif r == 1:
    #     return "paper"
    # else:
    #     return "scissors"

#print(choose_rps())

def RPS_game(player1, player2):
    if player1 == player2:
        print("It's a TIE!")
    elif player1 == "rock":
        if player2 == "paper":
            print("Player2 WIN!")
        else:
            print("Player1 WIN!")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player1 WIN!")
        else:
            print("Player2 WIN!")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player1 WIN!")
        else:
            print("Player2 WIN!")

def play_again():
    user_input = input("Would you like to play again? Yes or No\n")
    #r = random.choice([True, False])
    if user_input.lower() == "yes":
        return True
    elif user_input.lower() == "no":
        return False
    else:
        print("Invalid input")
        return False

def run_game():
    play = True
    while play:
        player1 = choose_rps()
        print(player1)
        player2 = choose_rps()
        print(player2)

        RPS_game(player1, player2)
        play = play_again()
        print("\n--------------\n")
    print("Thank you for playing!")

run_game()
