class Player:
    def __init__(self, name):
        self.name = name

    def guess_number(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                return guess
            except ValueError:
                print("Please enter a valid number.")
