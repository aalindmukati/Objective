import random

tries = 0
word_list = [
    "python", "galaxy", "wizard", "quartz", "avalanche", 
    "blizzard", "matrix", "oxygen", "voodoo", "unknown", 
    "jiujitsu", "luxury", "subway", "swivel", "avenue", 
    "gossip", "icebox", "microwave", "jackpot", "khaki"
]

gamed_name = random.choice(word_list)
print("Word list:", word_list)
print("-------------------------------------")
print("Guess a word from the word list")

while True:
    guess = input("Guess: ").lower()
    print("-------------------------------------")
    tries += 1
    
    if guess == gamed_name:
        print(f'Wow! You guessed the correct word, which was "{gamed_name}"!')
        print(f'It took you {tries} tries.')
        break
    else:
        print("Incorrect! Try again.")
