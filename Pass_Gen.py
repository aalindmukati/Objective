import random

alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

print("Welcome to Password Generator")
no_letters = int(input("Enter the number of letters "))
no_numbers = int(input("Enter the number of numbers(1-20 is the limit) "))
no_symbols = int(input("Enter the number of symbols "))

password = ''

for char in range(1,no_letters + 1):
    random_char = random.choice(alphabet_upper)
    password += random_char

for number in range(1,no_numbers + 1):
    random_number = random.choice(numbers)
    password += random_number

for symbol in range(1,no_symbols + 1):
    random_symbol = random.choice(symbols)
    password += random_symbol
    
print(password)