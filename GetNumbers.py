import random

class GetNumbers:
    
    numbers = []

    def __init__(self, number1, number2, number3, number4):

        self.numbers = []

        if (number1 >= 0 and number1 < 10):
            self.numbers.append(number1)

        if (number2 >= 0 and number2 < 10):
            self.numbers.append(number2)

        if (number3 >= 0 and number3 < 10):
            self.numbers.append(number3)

        if (number4 >= 0 and number4 < 10):
            self.numbers.append(number4)

    def sort(self):

        if (len(self.numbers) == 4):
            return random.sample(self.numbers, 4)
        else:
            return []
        
