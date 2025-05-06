import random
from modules.logo import logo
from modules.stages import stages
from modules.word_list import word_list

print(logo)

print("The fate of the hangman is in your hands!")

random_word = random.choice(word_list)
# print(f"Random word is {random_word}")

display = []

for char in random_word:
  display.append("_")

# print(display)

word_len = len(random_word)
# blank = word_len

end_of_game = False
remaining_lives = 6

while not end_of_game and remaining_lives > 0:
  user_guess = input("Guess a letter: ").lower()
  guess = False
  for index in range(len(random_word)):
    if user_guess == random_word[index]:
      display[index] = user_guess
      guess = True

  if not guess:
    remaining_lives -= 1
    print(f"Oops! '{user_guess}' isn't in the word. You lost a life.")

  print(f"{' '.join(display)}\n")
  print(stages[remaining_lives])

  if "_" not in display:
    end_of_game = True

  # print(remaining_lives)

display = ''.join(display) 

if display == random_word:
  print("Well done! You've survived the hangman and uncovered the word.")
else:
  print(f"Oh no! You're out of lives. The word was '{random_word}'. Better luck next time!")

# alternative
# while blank:
#   user_guess = input("Guess a letter: ").lower()
#   for index in range(len(random_word)):
#     if user_guess == random_word[index]:
#       display[index] = user_guess
#       blank-=1
#   print(display)

# for char in random_word:
#   if char == user_guess:
#     print("You guessed right.")
#   else:
#     print("You guessed wrong.")
