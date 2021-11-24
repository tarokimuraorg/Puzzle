class Formula:

    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0

    operator1 = ""
    operator2 = ""
    operator3 = ""

    def __init__(self, numbers, operators):

        self.number1 = numbers[0]
        self.number2 = numbers[1]
        self.number3 = numbers[2]
        self.number4 = numbers[3]

        self.operator1 = operators[0]
        self.operator2 = operators[1]
        self.operator3 = operators[2]

    def generate(self):
        
        formula1 = {"left":self.number1, "right":self.number2, "operator":self.operator1}
        formula2 = {"left":self.number2, "right":self.number3, "operator":self.operator2}
        formula3 = {"left":self.number3, "right":self.number4, "operator":self.operator3}

        formulas = []

        formulas.append(formula1)
        formulas.append(formula2)
        formulas.append(formula3)

        return formulas

    def output(self):

        if (self.operator1 == "*"):
            self.operator1 = "×"
        elif (self.operator1 == "/"):
            self.operator1 = "÷"

        if (self.operator2 == "*"):
            self.operator2 = "×"
        elif (self.operator2 == "/"):
            self.operator2 = "÷"

        if (self.operator3 == "*"):
            self.operator3 = "×"
        elif (self.operator3 == "/"):
            self.operator3 = "÷"

        formula = "{} {} {} {} {} {} {}".format(self.number1,
                                            self.operator1,
                                            self.number2,
                                            self.operator2,
                                            self.number3,
                                            self.operator3,
                                            self.number4)

        return formula
