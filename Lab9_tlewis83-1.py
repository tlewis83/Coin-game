"""
Coin Game
Tyee Lewis
October 26, 2025
Purpose:
    This program simulates a coin game.
    Two players each start with 20 coins and toss their coins each round.
    If the coins match, Player 1 wins a coin from Player 2.
    If the coins do not match, Player 2 wins a coin from Player 1.
    The game continues as long as the player chooses to play again.
"""

import random
from coin import Coin


def main():
    print("Welcome to the Match Coins Game!")
    print("Both players start with 20 coins.\n")

    # Create two Coin objects
    player1 = Coin()
    player2 = Coin()

    # Ask to play
    play_again = input("Would you like to play? (Y/N): ").strip().lower()

    while play_again == 'y':
        # Toss both coins
        player1.toss()
        player2.toss()

        # Display results
        print(f"\nPlayer 1 toss: {player1.get_sideup()}")
        print(f"Player 2 toss: {player2.get_sideup()}")

        # Compare results
        if player1.get_sideup() == player2.get_sideup():
            player1.set_amount(+1)
            player2.set_amount(-1)
            print("Coins matched! Player 1 wins this round.")
        else:
            player1.set_amount(-1)
            player2.set_amount(+1)
            print("Coins did NOT match! Player 2 wins this round.")

        # Display totals
        print(f"Player 1 total coins: {player1.get_amount()}")
        print(f"Player 2 total coins: {player2.get_amount()}")

        # Check for end conditions
        if player1.get_amount() <= 0 or player2.get_amount() <= 0:
            print("\nGame over!")
            break

        # Ask to continue
        play_again = input("\nWould you like to play again? (Y/N): ").strip().lower()

    # Final results
    print("\nFinal Results:")
    print(f"Player 1 total coins: {player1.get_amount()}")
    print(f"Player 2 total coins: {player2.get_amount()}")

    if player1.get_amount() > player2.get_amount():
        print("Player 1 wins the game!")
    elif player2.get_amount() > player1.get_amount():
        print("Player 2 wins the game!")
    else:
        print("It's a tie!")

    print("\nThanks for playing Match Coins!")


# Run the program
if __name__ == "__main__":
    main()
