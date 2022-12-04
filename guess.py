class Guess:
    taken = 0

    def getRand(self, start, end):
        from random import randint

        return randint(start, end)

    def setTaken(self):
        self.taken += 1

    def guessIsTooLow(self, playerGuess):
        if playerGuess < self.number:
            return True
        else:
            return False

    def guessIsTooHigh(self, playerGuess):
        if playerGuess > self.number:
            return True
        else:
            return False

    def guessIsOk(self, playerGuess):
        if playerGuess == self.number:
            return True
        else:
            return False


class Player:
    guess = 0

    def __init__(self, name):
        self.name = name
