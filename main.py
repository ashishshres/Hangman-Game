import random

print('''

                                                   ___                     
  /\\  /\\__ _ _ __   __ _ _ __ ___   __ _ _ __     / _ \\__ _ _ __ ___   ___ 
 / /_/ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\   / /_\\/ _` | '_ ` _ \\ / _ \\
/ __  / (_| | | | | (_| | | | | | | (_| | | | | / /_\\\\ (_| | | | | | |  __/
\\/ /_/ \\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_| \\____/\\__,_|_| |_| |_|\\___|
                   |___/                                                   

''')

word_list = ["apple", "breeze", "cloud", "wander", "echo", "flame", "mystery", "river", "spark", "twilight"]

random_word = random.choice(word_list)
# print(random_word)

user_guess = input("Guess a letter: ").lower()

for char in random_word:
  if char == user_guess:
    print("You guessed right.")
  else:
    print("You guessed wrong.")