"""
Hangman.

Authors: Hannah Meisner, Alyssa Taylor, Kaitlyn Wike.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def main():
    #Welcome
    print('HELLO!!')
    name = str(input('Whats your name: '))
    length = int(input('Enter MAXIMUM length for secret word:'))

    correct = ''
    for k in range(length):
        correct = correct + '-'

    tries = int(input('How many guesses do you want?'))
    triesLeft = tries
    word = random_word(length)
    guessedLetters = ''

    while triesLeft > 0:
        letter = guess(guessedLetters)
        guessedLetters = guessedLetters + letter
        triesLeft = checker(letter, word, triesLeft)
        correct = known(word, correct, letter)
        print(correct)
        if correct == word:
            print("You got it", name + "! Enjoy your prize of... nothing!")
            triesLeft = 0

    if correct != word:
        print("You lose", name + "! Outsmarted by a computer...")

    print("The word was:", word)


def random_word(length):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()

        while True:
            word = words[random.randrange(0, len(words))]
            if len(word) <= length:
                break

    return word


def guess(guessedLetters):
    letter = str(input('Enter your guess:'))
    while letter in guessedLetters:
        print("You already guessed that letter. Try again!")
        letter = letter = str(input('Enter your guess:'))

    return letter

def checker(letter, word, triesLeft):
    if letter in word:
        print('Guess Correct! You have', triesLeft, 'guess(es) remaining.')
    else:
        triesLeft = triesLeft - 1
        print('Incorrect! You have', triesLeft, 'guess(es) remaining.')

    return triesLeft


def known(word, correct, letter):
    new_correct = ''
    for k in range(len(word)):
        if correct[k] != '-':
            new_correct = new_correct + correct[k]
        elif word[k] == letter:
            new_correct = new_correct + word[k]
        else:
            new_correct = new_correct + '-'

    correct = new_correct
    return correct
main()