class GetFormulas:

    numbers = []
    operators = []

    def __init__(self, numbers, operators):

        self.numbers = numbers
        self.operators = operators

    def generate(self):
        
        formula1 = str(self.numbers[0]) + self.operators[0] + str(self.numbers[1])
        formula2 = str(self.numbers[1]) + self.operators[1] + str(self.numbers[2])
        formula3 = str(self.numbers[2]) + self.operators[2] + str(self.numbers[3])

        formulas = []

        formulas.append(formula1)
        formulas.append(formula2)
        formulas.append(formula3)

        return formulas
