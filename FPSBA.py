print("First price Based auction")
print('''-------------------------------------------------------------------------------------------------------------------------------------------------''')

Data = []

def user_Details():
    name = input('What is ur first name ')
    Bid = int(input('How much money u wanna bid '))
    User = {'name' : name , 'Bid' : Bid}
    Data.append(User)
    
def Result():
    winner = max(Data,key=lambda player: player['Bid'])
    print(winner)

while True:
    user_Details()
    Other = input("Any other players who wanna play (yes or no)").lower()
    
    if Other == "no":
        print('''-------------------------------------------------------------------------------------------------------------------------------------------------''')

        Result()
        break