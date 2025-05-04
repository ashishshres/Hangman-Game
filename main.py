import random

word_list = ["apple", "breeze", "cloud", "wander", "echo", "flame", "mystery", "river", "spark", "twilight"]

random_word = random.choice(word_list)
# print(random_word)

user_guess = input("Guess a letter: ").lower()

for char in random_word:
  if char == user_guess:
    print("You guessed right.")
  else:
    print("You guessed wrong.")