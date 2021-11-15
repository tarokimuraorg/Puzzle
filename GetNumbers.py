import random

class GetNumbers:
    
    numbers = []

    def __init__(self, numbers):

        self.numbers = numbers

    def sort(self):

        new_numbers = random.sample(self.numbers, 4)
        return new_numbers
