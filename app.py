# Rock, Paper, Scissors by Chamstick.
import random
import time

moveTable = ["rock", "paper", "scissors"]
choiceTable = ["yes", "no"]

gameRunning = True
gameMove = None

playerMove = None
playerWin = "lose"
playerResponse = "yes"

gameWin = 0
gameLose = 0
gameDraw = 0


while gameRunning: # All this does is make it so the code can repeat, enabling one to play many games quickly.

    gameMove = random.choice(moveTable)
    print("What is your move?")
    playerMove = input()
    while playerMove.casefold() not in moveTable:
        print("Sorry, that's not a valid move. Try again.")
        playerMove = input()

    # Checks if the game is a draw.
    if playerMove.lower() == gameMove:
        playerWin = "draw"
    elif playerMove.lower() != gameMove:

        # Runs if the player plays rock.
        if playerMove.lower() == "rock":
            if gameMove == "paper":
                playerWin = "lose"
            elif gameMove == "scissors":
                playerWin = "win"

        # Runs if the player plays paper.
        elif playerMove.lower() == "paper":
            if gameMove == "scissors":
                playerWin = "lose"
            elif gameMove == "rock":
                playerWin = "win"

        # Runs if the player plays scissors.
        elif playerMove.lower() == "scissors":
            if gameMove == "rock":
                playerWin = "lose"
            elif gameMove == "paper":
                playerWin = "win"

    # Runs if the player wins.
    if playerWin == "win":
        gameWin += 1
        print("You played: " + playerMove.lower())
        time.sleep(1)
        print("Game played: " + gameMove)
        time.sleep(1)
        print("You won. Congratulations!")
        print("W: " + str(gameWin))
        print("L: " + str(gameLose))
        print("D: " + str(gameDraw))
        print("Play again?")

    # Runs if the player loses.
    elif playerWin == "lose":
        gameLose += 1
        print("You played: " + playerMove.lower())
        time.sleep(1)
        print("Game played: " + gameMove)
        time.sleep(1)
        print("You lost. Better luck next time!")
        print("W: " + str(gameWin))
        print("L: " + str(gameLose))
        print("D: " + str(gameDraw))
        print("Play again?")

    # Runs if the game ends in a draw.
    elif playerWin == "draw":
        gameDraw += 1
        print("You played: " + playerMove.lower())
        time.sleep(1)
        print("Game played: " + gameMove)
        time.sleep(1)
        print("It's a draw!")
        print("W: " + str(gameWin))
        print("L: " + str(gameLose))
        print("D: " + str(gameDraw))
        print("Play again?")

    # This determines if the code should run again, or if the while loop should end.
    playerResponse = input()
    while playerResponse.casefold() not in choiceTable:
        print("Invalid response.")
        input()

    if playerResponse.lower() == "yes":
        continue
    elif playerResponse.lower() == "no":
        break
