class Calculator:

    leftnumber1 = 0
    leftnumber2 = 0
    leftnumber3 = 0

    rightnumber1 = 0
    rightnumber2 = 0
    rightnumber3 = 0

    inOperator1 = ""
    inOperator2 = ""
    inOperator3 = ""

    outOperator1 = ""
    outOperator2 = ""
    outOperator3 = ""
    
    answer = 0

    def __init__(self, formulas, answer):

        formula1 = formulas[0]
        formula2 = formulas[1]
        formula3 = formulas[2]

        self.leftnumber1 = formula1["left"]
        self.rightnumber1 = formula1["right"]

        self.leftnumber2 = formula2["left"]
        self.rightnumber2 = formula2["right"]

        self.leftnumber3 = formula3["left"]
        self.rightnumber3 = formula3["right"]

        self.inOperator1 = formula1["operator"]
        self.inOperator2 = formula2["operator"]
        self.inOperator3 = formula3["operator"]

        if (self.inOperator1 == "*"):
            self.outOperator1 = "×"
        elif (self.inOperator1 == "/"):
            self.outOperator1 = "÷"
        else:
            self.outOperator1 = self.inOperator1

        if (self.inOperator2 == "*"):
            self.outOperator2 = "×"
        elif (self.inOperator2 == "/"):
            self.outOperator2 = "÷"
        else:
            self.outOperator2 = self.inOperator2

        if (self.inOperator3 == "*"):
            self.outOperator3 = "×"
        elif (self.inOperator3 == "/"):
            self.outOperator3 = "÷"
        else:
            self.outOperator3 = self.inOperator3

        self.answer = answer

    def formula(self):

        if (self.isPattern1()):
            return self.formulaPattern1()
        elif (self.isPattern2()):
            return self.formulaPattern2()
        elif (self.isPattern3()):
            return self.formulaPattern3()
        else:
            return self.formulaPattern4()
        
    def formulaPattern1(self):

        result = "{} {} {} {} {} {} {}".format(self.leftnumber1,
                                            self.outOperator1,
                                            self.rightnumber1,
                                            self.outOperator2,
                                            self.rightnumber2,
                                            self.outOperator3,
                                            self.rightnumber3)

        return result

    def formulaPattern2(self):

        result = "( {} {} {} {} {} ) {} {}".format(self.leftnumber1,
                                            self.outOperator1,
                                            self.rightnumber1,
                                            self.outOperator2,
                                            self.rightnumber2,
                                            self.outOperator3,
                                            self.rightnumber3)

        return result

    def formulaPattern3(self):

        result = "{} {} ( {} {} {} {} {} )".format(self.leftnumber1,
                                            self.outOperator1,
                                            self.rightnumber1,
                                            self.outOperator2,
                                            self.rightnumber2,
                                            self.outOperator3,
                                            self.rightnumber3)

        return result

    def formulaPattern4(self):

        result = "( {} {} {} ) {} ( {} {} {} )".format(self.leftnumber1,
                                                       self.outOperator1,
                                                       self.rightnumber1,
                                                       self.outOperator2,
                                                       self.rightnumber2,
                                                       self.outOperator3,
                                                       self.rightnumber3)

        return result

    def isPattern1(self):
        
        resulto = 0

        if (self.inOperator1 == "*" or self.inOperator1 == "/"):

            if (self.inOperator1 == "*"):
                resulto = self.leftnumber1 * self.rightnumber1
            elif (self.inOperator1 == "/"):
                resulto = self.leftnumber1 / self.rightnumber1
            else:
                return False

            if (self.inOperator2 == "*" or self.inOperator2 == "/"):

                resultA1 = 0
                
                if (self.inOperator2 == "*"):
                    resultA1 = resulto * self.rightnumber2
                elif (self.inOperator2 == "/"):
                    resultA1 = resulto / self.rightnumber2
                else:
                    return False
                
                if (self.inOperator3 == "+"):
                    return (resultA1 + self.rightnumber3 == self.answer)
                elif (self.inOperator3 == "-"):
                    return (resultA1 - self.rightnumber3 == self.answer)
                elif (self.inOperator3 == "*"):
                    return (resultA1 * self.rightnumber3 == self.answer)
                elif (self.inOperator3 == "/"):
                    return (resultA1 / self.rightnumber3 == self.answer)
                else:
                    return False

            else:

                resultB1 = 0
                
                if (self.inOperator3 == "*" or self.inOperator3 == "/"):

                    if (self.inOperator3 == "*"):
                        resultB1 = self.leftnumber3 * self.rightnumber3
                    elif (self.inOperator3 == "/"):
                        resultB1 = self.leftnumber3 / self.rightnumber3

                    if (self.inOperator2 == "+"):
                        return (resulto + resultB1 == self.answer)
                    elif (self.inOperator2 == "-"):
                        return (resulto - resultB1 == self.answer)
                    else:
                        return False

                else:

                    resultC1 = 0
                    
                    if (self.inOperator2 == "+" or self.inOperator2 == "-"):
                        
                        if (self.inOperator2 == "+"):
                            resultC1 = resulto + self.rightnumber2
                        elif (self.inOperator2 == "-"):
                            resultC1 = resulto - self.rightnumber2
                        else:
                            return False

                        if (self.inOperator3 == "+"):
                            return (resultC1 + self.rightnumber3 == self.answer)
                        elif (self.inOperator3 == "-"):
                            return (resultC1 - self.rightnumber3 == self.answer)
                        else:
                            return False

                    else:
                        return False

        else:
            
            if (self.inOperator2 == "*" or self.inOperator2 == "/"):
                
                if (self.inOperator2 == "*"):
                    resulto = self.leftnumber2 * self.rightnumber2
                elif (self.inOperator2 == "/"):
                    resulto = self.leftnumber2 / self.rightnumber2
                else:
                    return False

                if (self.inOperator3 == "*" or self.inOperator3 == "/"):
                    
                    resultA2 = 0

                    if (self.inOperator3 == "*"):
                        resultA2 = resulto * self.rightnumber3
                    elif (self.inOperator3 == "/"):
                        resultA2 = resulto / self.rightnumber3
                    else:
                        return False

                    if (self.inOperator1 == "+"):
                        return (self.leftnumber1 + resultA2 == self.answer)
                    elif (self.inOperator1 == "-"):
                        return (self.leftnumber1 - resultA2 == self.answer)
                    else:
                        return False

                else:

                    if (self.inOperator1 == "+" or self.inOperator1 == "-"):

                        resultB2 = 0

                        if (self.inOperator1 == "+"):
                            resultB2 = self.leftnumber1 + resulto
                        elif (self.inOperator1 == "-"):
                            resultB2 = self.leftnumber1 - resulto
                        else:
                            return False

                        if (self.inOperator3 == "+"):
                            return (resultB2 + self.rightnumber3 == self.answer)
                        elif (self.inOperator3 == "-"):
                            return (resultB2 - self.rightnumber3 == self.answer)
                        else:
                            return False

                    else:
                        return False

            else:

                if (self.inOperator3 == "*" or self.inOperator3 == "/"):

                    if (self.inOperator3 == "*"):
                        resulto = self.leftnumber3 * self.rightnumber3
                    elif (self.inOperator3 == "/"):
                        resulto = self.leftnumber3 / self.rightnumber3
                    else:
                        return False

                    if (self.inOperator1 == "+" or self.inOperator1 == "-"):

                        resultA3 = 0
                        
                        if (self.inOperator1 == "+"):
                            resultA3 = self.leftnumber1 + self.rightnumber1
                        elif (self.inOperator1 == "-"):
                            resultA3 = self.leftnumber1 - self.rightnumber1
                        else:
                            return False

                        if (self.inOperator2 == "+" or self.inOperator2 == "-"):
                            
                            if (self.inOperator2 == "+"):
                                return (resultA3 + resulto == self.answer)
                            elif (self.inOperator2 == "-"):
                                return (resultA3 - resulto == self.answer)
                            else:
                                return False

                    else:
                        return False
                    
                else:

                    if (self.inOperator1 == "+" or self.inOperator1 == "-"):
                        
                        if (self.inOperator1 == "+"):
                            resulto = self.leftnumber1 + self.rightnumber1
                        elif (self.inOperator1 == "-"):
                            resulto = self.leftnumber1 - self.rightnumber1
                        else:
                            return False

                        resultA4 = 0

                        if (self.inOperator2 == "+" or self.inOperator2 == "-"):

                            if (self.inOperator2 == "+"):
                                resultA4 = resulto + self.rightnumber2
                            elif (self.inOperator2 == "-"):
                                resultA4 = resulto - self.rightnumber2
                            else:
                                return False

                            if (self.inOperator3 == "+" or self.inOperator3 == "-"):

                                if (self.inOperator3 == "+"):
                                    return (resultA4 + self.rightnumber3 == self.answer)
                                elif (self.inOperator3 == "-"):
                                    return (resultA4 - self.rightnumber3 == self.answer)
                            else:
                                return False

                        else:
                            return False

                    else:
                        return False

    def isPattern2(self):

        resulto = 0

        if (self.inOperator1 == "*" or self.inOperator1 == "/"):
            
            if (self.inOperator2 == "*" or self.inOperator2 == "/"):
                return False
                
            else:

                if (self.inOperator2 == "+" or self.inOperator2 == "-"):

                    if (self.inOperator1 == "*"):
                        resulto = self.leftnumber1 * self.rightnumber1
                    elif (self.inOperator1 == "/"):
                        resulto = self.leftnumber1 / self.rightnumber1
                    else:
                        return False

                    resulta1 = 0
                    
                    if (self.inOperator2 == "+"):
                        resulta1 = resulto + self.rightnumber2
                    elif (self.inOperator2 == "-"):
                        resulta1 = resulto - self.rightnumber2
                    else:
                        return False

                    if (self.inOperator3 == "+"):
                        return (resulta1 + self.rightnumber3 == self.answer)
                    elif (self.inOperator3 == "-"):
                        return (resulta1 - self.rightnumber3 == self.answer)
                    elif (self.inOperator3 == "*"):
                        return (resulta1 * self.rightnumber3 == self.answer)
                    elif (self.inOperator3 == "/"):
                        return (resulta1 / self.rightnumber3 == self.answer)
                    else:
                        return False

                else:
                    return False

        else:
            
            if (self.inOperator1 == "+" or self.inOperator1 == "-"):
                
                if (self.inOperator2 == "*" or self.inOperator2 == "/"):

                    if (self.inOperator2 == "*"):
                        resulto = self.leftnumber2 * self.rightnumber2
                    elif (self.inOperator2 == "/"):
                        resulto = self.leftnumber2 / self.rightnumber2
                    else:
                        return False

                    resulta2 = 0

                    if (self.inOperator1 == "+"):
                        resulta2 = self.leftnumber1 + resulto
                    elif (self.inOperator1 == "-"):
                        resulta2 = self.leftnumber1 - resulto
                    else:
                        return False

                    if (self.inOperator3 == "*"):
                        return (resulta2 * self.rightnumber3 == self.answer)
                    elif (self.inOperator3 == "/"):
                        return (resulta2 / self.rightnumber3 == self.answer)
                    elif (self.inOperator3 == "+"):
                        return (resulta2 + self.rightnumber3 == self.answer)
                    elif (self.inOperator3 == "-"):
                        return (resulta2 - self.rightnumber3 == self.answer)
                    else:
                        return False

                else:
                    
                    if (self.inOperator1 == "+"):
                        resulto = self.leftnumber1 + self.rightnumber1
                    elif (self.inOperator1 == "-"):
                        resulto = self.leftnumber1 - self.rightnumber1
                    else:
                        return False

                    resulta3 = 0

                    if (self.inOperator2 == "+"):
                        resulta3 = resulto + self.rightnumber2
                    elif (self.inOperator2 == "-"):
                        resulta3 = resulto - self.rightnumber2
                    else:
                        return False

                    if (self.inOperator3 == "*"):
                        return (resulta3 * self.rightnumber3 == self.answer)
                    elif (self.inOperator3 == "/"):
                        return (resulta3 / self.rightnumber3 == self.answer)
                    elif (self.inOperator3 == "+"):
                        return (resulta3 + self.rightnumber3 == self.answer)
                    elif (self.inOperator3 == "-"):
                        return (resulta3 - self.rightnumber3 == self.answer)
                    else:
                        return False

            else:
                return False

    def isPattern3(self):

        resulto = 0
        
        if (self.inOperator2 == "*" or self.inOperator2 == "/"):
            
            if (self.inOperator3 == "*" or self.inOperator3 == "/"):
                
                if (self.inOperator2 == "*"):
                    resulto = self.leftnumber2 * self.rightnumber2
                elif (self.inOperator2 == "/"):
                    resulto = self.leftnumber2 / self.rightnumber2
                else:
                    return False

                resulta1 = 0

                if (self.inOperator3 == "*"):
                    resulta1 = resulto * self.rightnumber3
                elif (self.inOperator3 == "/"):
                    resulta1 = resulto / self.rightnumber3
                else:
                    return False

                if (self.inOperator1 == "*"):
                    return (self.leftnumber1 * resulta1 == self.answer)
                elif (self.inOperator1 == "/"):
                    return (self.leftnumber1 / resulta1 == self.answer)
                else:
                    return False

            else:

                if (self.inOperator2 == "*"):
                    resulto = self.leftnumber2 * self.rightnumber2
                elif (self.inOperator2 == "/"):
                    resulto = self.leftnumber2 / self.rightnumber2
                else:
                    return False

                resulta2 = 0
                
                if (self.inOperator3 == "+"):
                    resulta2 = resulto + self.rightnumber3
                elif (self.inOperator3 == "-"):
                    resulta2 = resulto - self.rightnumber3
                else:
                    return False

                if (self.inOperator1 == "+"):
                    return (self.leftnumber1 + resulta2 == self.answer)
                elif (self.inOperator1 == "-"):
                    return (self.leftnumber1 - resulta2 == self.answer)
                elif (self.inOperator1 == "*"):
                    return (self.leftnumber1 * resulta2 == self.answer)
                elif (self.inOperator1 == "/"):
                    return (self.leftnumber1 / resulta2 == self.answer)
                else:
                    return False

        else:
            
            if (self.inOperator3 == "*" or self.inOperator3 == "/"):
                
                if (self.inOperator3 == "*"):
                    resulto = self.leftnumber3 * self.rightnumber3
                elif (self.inOperator3 == "/"):
                    resulto = self.leftnumber3 / self.rightnumber3
                else:
                    return False

                resulta3 = 0

                if (self.inOperator2 == "+"):
                    resulta3 = self.leftnumber2 + resulto
                elif (self.inOperator2 == "-"):
                    resulta3 = self.leftnumber2 - resulto
                else:
                    return False

                if (self.inOperator1 == "+"):
                    return (self.leftnumber1 + resulta3 == self.answer)
                elif (self.inOperator1 == "-"):
                    return (self.leftnumber1 - resulta3 == self.answer)
                elif (self.inOperator1 == "*"):
                    return (self.leftnumber1 * resulta3 == self.answer)
                elif (self.inOperator1 == "/"):
                    return (self.leftnumber1 / resulta3 == self.answer)
                else:
                    return False

            else:
                
                if (self.inOperator2 == "+"):
                    resulto = self.leftnumber2 + self.rightnumber2
                elif (self.inOperator2 == "-"):
                    resulto = self.leftnumber2 - self.rightnumber2
                else:
                    return False

                resulta4 = 0

                if (self.inOperator3 == "+"):
                    resulta4 = resulto + self.rightnumber3
                elif (self.inOperator3 == "-"):
                    resulta4 = resulto - self.rightnumber3
                else:
                    return False

                if (self.inOperator1 == "+"):
                    return (self.leftnumber1 + resulta4 == self.answer)
                elif (self.inOperator1 == "-"):
                    return (self.leftnumber1 - resulta4 == self.answer)
                elif (self.inOperator1 == "*"):
                    return (self.leftnumber1 * resulta4 == self.answer)
                elif (self.inOperator1 == "/"):
                    return (self.leftnumber1 / resulta4 == self.answer)
                else:
                    return False

    def isPattern4(self):
        
        resulta1 = 0

        if (self.inOperator1 == "+"):
            resulta1 = self.leftnumber1 + self.rightnumber1
        elif (self.inOperator1 == "-"):
            resulta1 = self.leftnumber1 - self.rightnumber1      
        elif (self.inOperator1 == "*"):
            resulta1 = self.leftnumber1 * self.rightnumber1
        elif (self.inOperator1 == "/"):
            resulta1 = self.leftnumber1 / self.rightnumber1
        else:
            return False

        resultb1 = 0

        if (self.inOperator3 == "+"):
            resultb1 = self.leftnumber3 + self.rightnumber3
        elif (self.inOperator3 == "-"):
            resultb1 = self.leftnumber3 - self.rightnumber3
        elif (self.inOperator3 == "*"):
            resultb1 = self.leftnumber3 * self.rightnumber3
        elif (self.inOperator3 == "/"):
            resultb1 = self.leftnumber3 / self.rightnumber3
        else:
            return False

        if (self.inOperator2 == "+"):
            return (resulta1 + resultb1 == self.answer)
        elif (self.inOperator2 == "-"):
            return (resulta1 - resultb1 == self.answer)
        elif (self.inOperator2 == "*"):
            return (resulta1 * resultb1 == self.answer)
        elif (self.inOperator2 == "/"):
            return (resulta1 / resultb1 == self.answer)
        else:
            return False
