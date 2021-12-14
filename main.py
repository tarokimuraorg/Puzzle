from GetNumbers import GetNumbers
from GetOperator import GetOperator
from Calculator import Calculator
from GetFormulas import GetFormulas

if __name__ == "__main__":

    answer = 10
    formula = None
    cnt = 0

    while (formula is None):
    
        numbers = GetNumbers(3,4,7,8).sort()
        operators = GetOperator().select()
        formulas = GetFormulas(numbers, operators).generate()
    
        formula = Calculator(formulas, answer).formula()
        cnt += 1

        if (cnt == 3000):
            break

    if (formula is None):
        print("formula : not found")
    else:
        print("{} = {}".format(formula, answer))
        
