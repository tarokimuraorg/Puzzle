import random

class GetOperator:
    
    operators = []

    def __init__(self):

        self.operators.append("+")
        self.operators.append("-")
        self.operators.append("*")
        self.operators.append("/")

    def select(self):

        selected_operators = random.choices(self.operators, k=3)
        return selected_operators
