import random

operators = ["+","-","*","/"]
numbers = [3,4,7,8]

new_numbers = random.sample(numbers, 4)

for number in new_numbers:
    print(number)
