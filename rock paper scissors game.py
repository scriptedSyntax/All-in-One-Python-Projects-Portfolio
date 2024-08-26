import random

while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock,paper or scissors? ").lower()

    if player == computer:
        print("player picked: ", player)
        print("computer picked: ", computer)
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player picked: ", player)
            print("computer picked: ", computer)
            print("Win!")
        if computer == "paper":
            print("player picked: ", player)
            print("computer picked: ", computer)
            print("Lose!")
    elif player == "paper":
        if computer == "scissors":
            print("player picked: ", player)
            print("computer picked: ", computer)
            print("Lose!")
        if computer == "rock":
            print("player picked: ", player)
            print("computer picked: ", computer)
            print("Win!")
    elif player == "scissors":
        if computer == "paper":
            print("player picked: ", player)
            print("computer picked: ", computer)
            print("Win!")
        if computer == "rock":
            print("player picked: ", player)
            print("computer picked: ", computer)
            print("Lose!")

    play_again = input("do you want to play again? (yes/no)").lower()
    if play_again != "yes":
        break
print("Bye!")