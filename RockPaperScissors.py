import random

choices = ["rock","paper","scissors"]
running = True

name = input("Welcome to a interactive Rock Paper Scissors game! What is your name?: ")
print("Hello, " + name + "!")

def play_game(player_choice):
    computer_choice = random.choice(choices)
    print("The computer chose: " + computer_choice)
    print("Your choice is: " + player_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissor") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")



while running:
    print("\nChoices: ROCK, PAPER, SCISSOR")
    player_choice = input("Please input your choice: ")
    if player_choice == "rock":
        play_game("rock")
    elif player_choice == "paper":
        play_game("paper")
    elif player_choice == "scissors":
        play_game("scissors")
    else:
        print("Wrong choice.")
