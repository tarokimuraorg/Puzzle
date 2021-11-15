import random

class GetOperator:
    
    operators = []

    def __init__(self):

        self.operators.append("+")
        self.operators.append("-")
        self.operators.append("*")
        self.operators.append("/")

    def select(self):
        
        selected_operator = random.choice(self.operators)
        return selected_operator
