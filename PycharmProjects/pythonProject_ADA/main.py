import random

def choose_rps():
    return random.choice(["rock", "paper", "scissors"])

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

def run_game_n_times(n):
    for i in range(n):
        print(f"Game number {i+1}")
        player1 = choose_rps()
        print(player1)
        player2 = choose_rps()
        print(player2)

        RPS_game(player1, player2)
        print("\n--------------\n")
    print("Thank you for playing!")

input_n = input("How many time would you like to play?\n")
run_game_n_times(int(input_n))
