# This creates a file named 'example.txt' and writes text to it
# with open("example.txt", "w", encoding="utf-8") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a new line of text.")
try:
    file = open('a_new.txt')
except:
    file = open("a_new.txt", 'w')
    file.write('namaskar')
finally:
    file.close()