class Game:
    def __init__(self, target_number):
        self.target_number = target_number

    def check_guess(self, guess):
        if guess == self.target_number:
            return "Congratulations! You guessed the number correctly!"
        elif guess < self.target_number:
            return "The number is higher. Try again!"
        else:
            return "The number is lower. Try again!"
