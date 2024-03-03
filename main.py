from zenith_tea.game_logic import Game
from zenith_tea.player import Player
from zenith_tea.utils import generate_target_number

def main():
    print("Welcome to Zenith Tea Number Guessing Game!")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    target_number = generate_target_number()
    game = Game(target_number)

    while True:
        guess = player.guess_number()
        result = game.check_guess(guess)
        print(result)
        if guess == target_number:
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
