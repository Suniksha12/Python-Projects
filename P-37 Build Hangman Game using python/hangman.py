import random

words = ["UMBRELLA", "COMPUTER","TELESCOPE","SMARTPHONE"]
word = random.choice(words)

total_chances = 7

guessed_word = "-"*len(word)

print(guessed_word)
letter = input("Guess a Letter: ").upper()
if letter in word:
    for index in range(len(word)):
        if word[index] == letter:
            guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
            print(guessed_word)