print("hello Welcome to the ainway ainway pizza shop")
bill = 0
pizza = input("Which pizza would u like Small(S) , Medium(M) , Large(L): ")

if pizza == "S":
    bill += 10
elif pizza == "M":
    bill += 15
elif pizza == "L":
    bill += 20

toppings = input("Would u like some cheese(Say Yes) ")

if toppings == "Yes":
    bill += 3

print(f"Your total bill is ${bill}")
