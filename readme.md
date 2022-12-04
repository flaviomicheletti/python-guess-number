![image](https://user-images.githubusercontent.com/1257048/205497361-7eed175c-5323-46ef-9c38-34c2733f3da5.png)

# Intro

It is a console game written in Python.

The original you can find on the website 
[http://inventwithpython.com/chapter4.html](http://inventwithpython.com/chapter4.html)

Playing...

    game:    Hello! What is your name?
    player:  Albert
    game:    Well, Albert, I am thinking of a number between 1 and 20.
    game:    Take a guess.
    player:  10
    game:    Your guess is too high.
    game:    Take a guess.
    player:  2
    game:    Your guess is too low.
    game:    Take a guess.
    player:  4
    game:    Good job, Albert! You guessed my number in 3 guesses!


## Environment

    python3 -m venv venv
    . venv/bin/activate

In order to run coverage you will have to install it.

    pip install coverage


## To run the game

Assuming you are on __Linux__ and already have __Python__ installed.

    python terminal.py


## Running the tests

    python -m unittest guess-number.py -v


## Running the coverage

    python -m coverage run -m unittest guess-number.py
    python -m coverage report
    python -m coverage html


## Procedural version

For such a small problem, procedural programming would be enough.

It's no wonder that OOP is said to introduce complexity.

    python procedure-version.py
