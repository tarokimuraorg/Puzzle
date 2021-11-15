import random

class GetNumbers:
    
    numbers = []

    def __init__(self, number1, number2, number3, number4):

        self.numbers.append(number1)
        self.numbers.append(number2)
        self.numbers.append(number3)
        self.numbers.append(number4)

    def sort(self):
        
        new_numbers = random.sample(self.numbers, 4)
        return new_numbers
