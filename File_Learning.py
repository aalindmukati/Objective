with open("names.txt") as names_file:
    name = names_file.read().splitlines()

PLACEHOLDER = '[name]'

with open("file.txt") as letter:
    letter_content = letter.read()
    for name in name:
        updated_letter = letter_content.replace(PLACEHOLDER, name)
        print(updated_letter)