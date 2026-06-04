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

def calculate_score(hand):
    score = 0
    ace_count = hand.count('A')
    
    # Add up the raw dictionary values
    for card in hand:
        score += blackjack_values[card]
        
    # If the score is over 21 and we have Aces, turn 11s into 1s
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
        
    return score

User_score = calculate_score(User_card)
user_playing = True

while user_playing:
    User_score = calculate_score(User_card)
    print(f'Your Current score is{User_score}')

    if User_score >= 21:
        break
    choice = input(f"Would u like to hit or stand ").lower()

    if choice == "hit":
        pata = random.choice(list(blackjack_values))
        User_card.append(pata)
        print(User_card)
    elif choice == 'stand':
        user_playing = False
    else:
        print("Invalid input. Please type 'hit' or 'stand'.")