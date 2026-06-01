random_numbers = [263, 128, 106, 289, 170, 162, 157, 135, 288, 126, 273, 289, 239, 122, 251, 208, 108, 107, 123, 155]

max_score = 0

for score in random_numbers:
    if score>max_score:
        max_score=score

print(max_score)
max_score = max(random_numbers)

print(max_score)