import random

print("---------------------")
print("Welcome to BlackJack")
print("---------------------")
blackjack_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', 'A']

User_card=[]

choice = input("Would u like to hit or stand ").lower()
if choice == 'hit':
    pata = random.choice(blackjack_values)
    User_card.append(pata)


print(User_card)