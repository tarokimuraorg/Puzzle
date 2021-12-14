class GetFormulas:

    numbers = []
    operators = []

    def __init__(self, numbers, operators):

        self.numbers = numbers
        self.operators = operators

    def generate(self):

        formulas = []

        if (len(self.numbers) == 4):
        
            formula1 = {"left":self.numbers[0], "right":self.numbers[1], "operator":self.operators[0]}
            formula2 = {"left":self.numbers[1], "right":self.numbers[2], "operator":self.operators[1]}
            formula3 = {"left":self.numbers[2], "right":self.numbers[3], "operator":self.operators[2]}

            formulas.append(formula1)
            formulas.append(formula2)
            formulas.append(formula3)

        return formulas
    
