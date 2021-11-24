import random

class GetNumbers:
    
    numbers = []

    def __init__(self, number1, number2, number3, number4):

        self.numbers = [number1,number2,number3,number4]

    def sort(self):

        new_numbers = random.sample(self.numbers, 4)
        return new_numbers
