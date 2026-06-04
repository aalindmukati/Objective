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
    
    for card in hand:
        score += blackjack_values[card]
        
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
        
    return score

user_playing = True

while user_playing:
    User_score = calculate_score(User_card)
    print(f"Your current score is: {User_score}")
    
    if User_score >= 21:
        break

    choice = input("Would u like to hit or stand ").lower()

    if choice == 'hit':
        pata = random.choice(list(blackjack_values))
        User_card.append(pata)
        print(User_card)
    elif choice == 'stand':
        user_playing = False
    else:
        print("Invalid input. Please type 'hit' or 'stand'.")

User_score = calculate_score(User_card)

if User_score > 21:
    print(f'the Computer card is {Comp_card}')
    print("Sorry man u loose")
else:
    Comp_score = calculate_score(Comp_card)
    
    while Comp_score < 17:
        pata = random.choice(list(blackjack_values))
        Comp_card.append(pata)
        Comp_score = calculate_score(Comp_card)
        
    print(f"\nThe Final Computer hand is {Comp_card} with a score of: {Comp_score}")
    
    if Comp_score > 21:
        print("The Computer busted! You win! 🎉")
    elif User_score > Comp_score:
        print("You have a higher score than the Computer! You win! 🎉")
    elif User_score < Comp_score:
        print("The Computer has a higher score. You lose. 😞")
    else:
        print("It's a tie (Push)! 🤝")
