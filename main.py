from GetNumbers import GetNumbers
from GetOperator import GetOperator
from Calculator import Calculator
from GetFormulas import GetFormulas

if __name__ == "__main__":

    answer = 10
    formula = None
    cnt = 0

    objNumbers = GetNumbers(3,4,7,8)
    objOperator = GetOperator()

    while (formula is None):

        numbers = objNumbers.sort()
        operators = objOperator.select()

        objFormulas = GetFormulas(numbers, operators)
        formulas = objFormulas.generate()
    
        objCalculator = Calculator(formulas, answer)
        formula = objCalculator.formula()

        cnt += 1

        if (cnt == 3000):
            break

    if (formula is None):
        print("formula : not found")
    else:
        print("{} = {}".format(formula, answer))
        
