print("First price Based auction")
print('''-------------------------------------------------------------------------------------------------------------------------------------------------''')

Data = []

def user_Details():
    name = input('What is ur first name ')
    Bid = int(input('How much money u wanna bid '))
    User = {'name' : name , 'Bid' : Bid}
    Data.append(User)
    

user_Details()

Other = input("Any other players who wanna play ").lower()

while Other == "yes":
    user_Details()