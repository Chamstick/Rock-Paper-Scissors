# Rock, Paper, Scissors by Chamstick.
import random
import time


moveTable = ["rock", "paper", "scissors"]
choiceTable = ["yes", "no"]

gameRunning = True

playerMove = "rock"
playerWin = "lose"
playerResponse = "yes"

gameWin = 0
gameLose = 0
gameDraw = 0

while gameRunning:
    gameMove = random.choice(moveTable)
    print("What is your move?")
    playerMove = input()

    while playerMove.casefold() not in moveTable:
        print("Sorry, that's not a valid move. Try again.")
        playerMove = input()

    # Checks if the game is a draw.
    if str(playerMove.casefold()) == str(gameMove):
        playerWin = "Draw"
        while playerResponse.casefold() not in choiceTable:
            print("Invalid response.")
            playerResponse = input()
    elif playerMove.casefold() != gameMove:

        # Runs if the player plays rock.
        if playerMove.casefold() == "Rock":
            if gameMove == "Paper":
                playerWin = "Lose"
            elif gameMove == "Scissors":
                playerWin = "Win"

        # Runs if the player plays paper.
        elif playerMove.casefold() == "Paper":
            if gameMove == "Scissors":
                playerWin = "Lose"
            elif gameMove == "Rock":
                playerWin = "Win"

        # Runs if the player plays scissors.
        elif playerMove.casefold() == "Scissors":
            if gameMove == "Rock":
                playerWin = "Lose"
            elif gameMove == "Paper":
                playerWin = "Win"

    if playerWin == "Win":
        gameWin += 1
        print("You played: " + playerMove.casefold())
        time.sleep(1)
        print("Game played: " + gameMove)
        time.sleep(1)
        print("You won. Congratulations!")
        print("W: " + str(gameWin))
        print("L: " + str(gameLose))
        print("D: " + str(gameDraw))
        print("Play again?")

    elif playerWin == "Lose":
        gameLose += 1
        print("You played: " + playerMove.casefold())
        time.sleep(1)
        print("Game played: " + gameMove)
        time.sleep(1)
        print("You lost. Better luck next time!")
        print("W: " + str(gameWin))
        print("L: " + str(gameLose))
        print("D: " + str(gameDraw))
        print("Play again?")

    elif playerWin == "Draw":
        gameDraw += 1
        print("You played: " + playerMove.casefold())
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

    if playerResponse.casefold() == "yes":
        continue
    elif playerResponse.casefold() == "no":
        break
