import random
print("Welcome to the RockPaperScissors Game! \nIt's kind of basic, but should do the trick. \ntype in rock, paper, or scissors, and we'll try to beat you! \n\nTo Leave type EXIT\n\nTo play type:\nRock\nPaper\nScissors")
playerPoints = 0
computerPoints = 0
playerInput = ""
computerInput = ["rock","paper", "scissors"]
while playerInput != "exit" and playerPoints != 3 and computerPoints != 3:
    playerInput = input()
    computerChoice = computerInput[random.randint(0,2)]
    print(computerChoice)
    if playerInput == computerChoice:
        print(f"You both chose {playerInput}!\nYour points: {playerPoints}\nComputer points: {computerPoints}")
    elif playerInput == "rock":
        if computerChoice == "scissors":
            playerPoints += 1
            print(f"Rock beats scissors!\nYour points: {playerPoints}\nComputer points: {computerPoints}")
        else:
            computerPoints += 1
            print(f"Paper beats rock, Sorry!\nYour points: {playerPoints}\nComputer points: {computerPoints}")
    elif playerInput == "paper":
        if computerChoice == "rock":
            playerPoints += 1
            print(f"Rock beats scissors!\nYour points: {playerPoints}\nComputer points: {computerPoints}")
        else:
            computerPoints += 1
            print(f"Paper beats rock, Sorry!\nYour points: {playerPoints}\nComputer points: {computerPoints}")
    elif playerInput == "scissors":
        if computerChoice == "paper":
            playerPoints += 1
            print(f"Rock beats scissors!\nYour points: {playerPoints}\nComputer points: {computerPoints}")
        else:
            computerPoints += 1
            print(f"Paper beats rock, Sorry!\nYour points: {playerPoints}\nComputer points: {computerPoints}")
if playerPoints > computerPoints:
    print("You win! Game over!")
else:
    print("You Lose! Game over!")


    
