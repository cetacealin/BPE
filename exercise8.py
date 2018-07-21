import sys
'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock'''

def compare(player1, player2):
    if player1 == player2:
        return ("It's a tie!")
    elif player1 == "Rock":
        if player2 == "Sissors":
            return ("Player1 wins!")
        else:
            return ("Player2 wins!")
    elif player1 == "Sissors":
        if player2 == "Paper":
            return ("Player1 wins!")
        else:
            return ("Player2 wins!")
    elif player1 == "Paper":
        if player2 == "Rock":
            return ("Player1 wins!")
        else:
            return ("Player2 wins!")
    else:
        return ("Invalid input!")
        sys.exit()

p1 = input("First player; Rock, Scissors, Paper: ")
p2 = input("Second player; Rock, Scissors, Paper: ")
print(compare(p1, p2))

