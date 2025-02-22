import random


def get_player_choice():
    # Gets the player's choice (rock, paper, scissors or quit).
    while True:
        choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
        if choice in ["rock", "paper", "scissors", "q"]:
            return choice
        else:
            print("Invalid choice. Please try again.")


def get_computer_choice():
    # Randomly generates the computer's choice.
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player_choice, computer_choice):
    # Determines the winner of a single round.
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        return "tie"
    elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "player"
    else:
        return "computer"


def play_game():
    player_score = 0
    computer_score = 0

    # Exit the game loop if the player chooses to quit
    while True:
        player_choice = get_player_choice()
        if player_choice == 'q':
            break

        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score: Player {player_score} - Computer {computer_score}\n")  # Display the current score

    print("Game Over!")
    print(f"Final Score: Player {player_score} - Computer {computer_score}")

    if player_score > computer_score:
        print("You are the winner!")
    elif computer_score > player_score:
        print("The computer is the winner!")
    else:
        print("The game ended in a tie.")


if __name__ == "__main__":
    play_game()