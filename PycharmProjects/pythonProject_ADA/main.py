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

player1 = choose_rps()
print(player1)
player2 = choose_rps()
print(player2)

RPS_game(player1, player2)