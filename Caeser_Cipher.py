print('''-------------------------------------------------------------------------------------------------------------------------------------------------
''')
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = int(input(f"if u want to Encrypt press {1} and to Decrypt press {2} "))
text = input("Enter your message here ").lower()
number = int(input('By how many numeric values u wanna encrypt '))

#-------------------------------------------------------------------------------------------------------------------------------------------------

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        
        shifted_pos = (alphabet_list.index(letter) + shift_amount) % 26
        
        cipher_text += alphabet_list[shifted_pos]
        
    print(f"here is the encoded result: {cipher_text}")



def decrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        
        shifted_pos = (alphabet_list.index(letter) - shift_amount) % 26
        
        cipher_text += alphabet_list[shifted_pos]
        
    print(f"here is the decoded result: {cipher_text}")


