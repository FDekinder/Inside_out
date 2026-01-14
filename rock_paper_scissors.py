"""Rock Paper Scissors Game"""
import random

def play():
    choices = ["rock", "paper", "scissors"]
    score = {"player": 0, "computer": 0}

    print("Rock Paper Scissors!")
    print("Type 'quit' to exit.\n")

    while True:
        player = input("Choose rock, paper, or scissors: ").lower()

        if player == "quit":
            print(f"\nFinal Score - You: {score['player']}, Computer: {score['computer']}")
            break

        if player not in choices:
            print("Invalid choice. Try again.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
            score["player"] += 1
        else:
            print("Computer wins!")
            score["computer"] += 1

        print(f"Score - You: {score['player']}, Computer: {score['computer']}\n")

if __name__ == "__main__":
    play()
