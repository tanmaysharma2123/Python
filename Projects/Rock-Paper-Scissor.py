import random

moves = ["rock", "paper", "scissor"]


def move(moves, player1_move, randomNumber):
    player2_move = moves[randomNumber]

    if (player2_move == "rock"):

        print("Computer chooses rock!\n")

        if (player1_move == "paper"):
            return "Paper beats Rock!, you won."

        elif (player1_move == "scissor"):
            return "Rock beats Scissor, Computer won."

        else:
            return "It's a tie."

    elif (player2_move == "paper"):

        print("Computer chooses paper!\n")

        if (player1_move == "rock"):
            return "Paper beats Rock!, Computer won."

        elif (player1_move == "scissor"):
            return "Scissor beats Paper!, you won."

        else:
            return "It's a tie."

    else:

        print("Computer chooses scissor!\n")

        if (player1_move == "rock"):
            return "Rock beats Scissor, you won."

        elif (player1_move == "paper"):
            return "Scissor beats Rock!, Computer won."

        else:
            return "It's a tie."


player1_move = input("Enter your move: ")
print("-------------------------|")

randomNumber = random.randint(0, 2)

print(move(moves, player1_move, randomNumber))
