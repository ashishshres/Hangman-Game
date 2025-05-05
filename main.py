import random

print('''

                                                   ___                     
  /\\  /\\__ _ _ __   __ _ _ __ ___   __ _ _ __     / _ \\__ _ _ __ ___   ___ 
 / /_/ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\   / /_\\/ _` | '_ ` _ \\ / _ \\
/ __  / (_| | | | | (_| | | | | | | (_| | | | | / /_\\\\ (_| | | | | | |  __/
\\/ /_/ \\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_| \\____/\\__,_|_| |_| |_|\\___|
                   |___/                                                   

''')

print("The fate of the hangman is in your hands!")

stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

word_list = [
    "apple", "ant", "anchor", "arrow", "apricot", "artist", "album", "alarm", "ankle", "astronaut",
    "banana", "basket", "button", "bottle", "bridge", "blanket", "breeze", "bucket", "bubble", "biscuit",
    "camera", "candle", "castle", "circle", "cactus", "cookie", "curtain", "crystal", "cabinet", "carpet",
    "dragon", "donkey", "desert", "drawer", "diamond", "doctor", "drum", "dolphin", "danger", "dustbin",
    "eagle", "earth", "elbow", "engine", "energy", "elephant", "envelope", "eraser", "echo", "eclipse",
    "flower", "forest", "finger", "feather", "family", "fence", "flute", "flag", "fox", "freedom",
    "guitar", "garden", "globe", "garage", "grape", "goose", "gold", "glass", "glove", "gate",
    "house", "hammer", "helmet", "hippo", "honey", "hill", "holiday", "horse", "hook", "harbor",
    "island", "iceberg", "igloo", "insect", "idea", "inch", "icon", "input", "item", "issue",
    "jungle", "jacket", "jewel", "joker", "jigsaw", "jelly", "jogger", "journal", "jar", "jam",
    "kite", "kangaroo", "keyboard", "kitchen", "kitten", "kettle", "king", "knife", "knot", "kayak",
    "lemon", "ladder", "lantern", "laptop", "lizard", "library", "lamb", "leaf", "lock", "light",
    "monkey", "mountain", "mirror", "magnet", "motor", "mango", "mouse", "mask", "menu", "magic",
    "notebook", "needle", "nest", "night", "nail", "noise", "narrow", "name", "net", "number",
    "ocean", "orange", "ostrich", "oven", "object", "orbit", "owl", "onion", "oil", "oxygen",
    "pencil", "panda", "pillow", "planet", "poster", "paint", "pan", "pumpkin", "pearl", "parrot",
    "queen", "quilt", "quiz", "quiver", "quartz", "quote", "queue", "quack", "quiet", "quick",
    "rabbit", "rocket", "rainbow", "river", "robot", "ruler", "rose", "ring", "road", "rope",
    "sun", "star", "school", "spoon", "ship", "shadow", "socks", "stone", "sand", "swan",
    "tiger", "table", "train", "truck", "tent", "tooth", "tower", "towel", "tap", "tool",
    "umbrella", "uniform", "unicorn", "utensil", "urban", "umpire", "update", "unit", "uplift", "usage",
    "violin", "village", "vase", "van", "vest", "vulture", "vacuum", "valley", "voice", "vote",
    "whale", "window", "water", "wagon", "wheel", "wolf", "wall", "wing", "watch", "wind",
    "xylophone", "xenon", "xylem", "xerox", "xenial", "xenolith", "xanthic", "xenogeny", "xiphoid", "xenopus",
    "yacht", "yak", "yellow", "yawn", "yarn", "yogurt", "yolk", "year", "yesterday", "yard",
    "zebra", "zoo", "zipper", "zero", "zinc", "zone", "zigzag", "zest", "zeal", "zodiac"
]

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

  print(f"{' '.join(display)}\n")

  if not guess:
    remaining_lives -= 1
    print(stages[remaining_lives])

  if "_" not in display:
    end_of_game = True

  # print(remaining_lives)

display = ''.join(display) 

if display == random_word:
  print("You win!")
else:
  print("You loose!")

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
