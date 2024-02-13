rock_paper_scissors_defeat = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}
assert rock_paper_scissors_defeat.get('rock') == 'scissors', "rock should defeat scissors"
assert rock_paper_scissors_defeat.get('paper') == 'rock', "paper should defeat rock"
assert rock_paper_scissors_defeat.get('scissors') == 'paper', "scissors should defeat paper"

for key in rock_paper_scissors_defeat:
    print(f'{key} defeats {rock_paper_scissors_defeat[key]}')
print("Your solution works!")

player1 = "paper"
player2 = "rock"

if player1 == player2:
    print("It's a TIE!")
elif player1 == "rock":
    if player2 == rock_paper_scissors_defeat['rock']:
        print("Player1 WIN!")
    else:
        print("Player2 WIN!")
elif player1 == "paper":
    if player2 == rock_paper_scissors_defeat['paper']:
        print("Player1 WIN!")
    else:
        print("Player2 WIN!")
elif player1 == "scissors":
    if player2 == rock_paper_scissors_defeat['scissors']:
        print("Player1 WIN!")
    else:
        print("Player2 WIN!")