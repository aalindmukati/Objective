import random

print("---------------------")
print("Welcome to BlackJack")
print("---------------------")
blackjack_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'A': 11
}


User_card=[]
Comp_card =[]

for _ in range(2):
    pata = random.choice(list(blackjack_values)) 
    User_card.append(pata)

print(f'the User card is {User_card}')

for _ in range(2):
    pata = random.choice(list(blackjack_values))
    Comp_card.append(pata)

choice = input("Would u like to hit or stand ").lower()
if choice == 'hit':
    pata = random.choice(list(blackjack_values))
    User_card.append(pata)
    print(User_card)
else:
    print(f'the Computer card is {Comp_card}')