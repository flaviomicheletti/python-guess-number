import unittest
from guess import *

class GuessTest(unittest.TestCase):
    def testRand(self):

        guess = Guess()
        guess.rangeStart = 1
        guess.rangeEnd = 20

        randoNumber = guess.getRand(guess.rangeStart, guess.rangeEnd)
        self.assertTrue(randoNumber >= 1 and randoNumber <= 20)

    def testSetTaken(self):
        guess = Guess()
        self.assertEqual(0, guess.taken)

        guess.setTaken()
        guess.setTaken()
        guess.setTaken()
        self.assertEqual(3, guess.taken)

    def testGuessIsTooLow(self):
        player = Player("foo")

        guess = Guess()
        guess.number = 12

        player.guess = 8
        self.assertTrue(guess.guessIsTooLow(player.guess))

        player.guess = 16
        self.assertFalse(guess.guessIsTooLow(player.guess))

    def testGuessIsTooHigh(self):
        player = Player("foo")

        guess = Guess()
        guess.number = 12

        player.guess = 14
        self.assertTrue(guess.guessIsTooHigh(player.guess))

        player.guess = 10
        self.assertFalse(guess.guessIsTooHigh(player.guess))

    def testGuessIsOk(self):
        player = Player("foo")

        guess = Guess()
        guess.number = 12

        player.guess = 12
        self.assertTrue(guess.guessIsOk(player.guess))

        player.guess = 13
        self.assertFalse(guess.guessIsOk(player.guess))
