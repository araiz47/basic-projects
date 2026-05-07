#hangman 1st version 

import random

word = ["apple","banana","mango","strawberry"]
random_word = random.choice(word)
show = []

for letter in random_word:
    show.append('_')
print(show)


while "_" in show:
    guess = input("Enter a word: ").lower()
    for position in range(len(random_word)):
        if random_word[position] == guess:
            show[position] = guess
    print(show)
print("You won")
    