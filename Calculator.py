class Calculator:

    formulas = []

    def __init__(self, formulas):

        self.formulas = formulas

    def run(self):
        
        formula1 = self.formulas[0]
        formula2 = self.formulas[1]
        formula3 = self.formulas[2]

        leftnumber1 = formula1["left"]
        rightnumber1 = formula1["right"]

        leftnumber2 = formula2["left"]
        rightnumber2 = formula2["right"]

        leftnumber3 = formula3["left"]
        rightnumber3 = formula3["right"]

        operator1 = formula1["operator"]
        operator2 = formula2["operator"]
        operator3 = formula3["operator"]

        resulto = 0

        if (operator1 == "*" or operator1 == "/"):

            if (operator1 == "*"):
                resulto = leftnumber1 * rightnumber1
            elif (operator1 == "/"):
                resulto = leftnumber1 / rightnumber1
            else:
                return None

            if (operator2 == "*" or operator2 == "/"):

                resultA1 = 0
                
                if (operator2 == "*"):
                    resultA1 = resulto * rightnumber2
                elif (operator2 == "/"):
                    resultA1 = resulto / rightnumber2
                else:
                    return None
                
                if (operator3 == "+"):
                    return resultA1 + rightnumber3
                elif (operator3 == "-"):
                    return resultA1 - rightnumber3
                elif (operator3 == "*"):
                    return resultA1 * rightnumber3
                elif (operator3 == "/"):
                    return resultA1 / rightnumber3
                else:
                    return None

            else:

                resultB1 = 0
                
                if (operator3 == "*" or operator3 == "/"):

                    if (operator3 == "*"):
                        resultB1 = leftnumber3 * rightnumber3
                    elif (operator3 == "/"):
                        resultB1 = leftnumber3 / rightnumber3

                    if (operator2 == "+"):
                        return resulto + resultB1
                    elif (operator2 == "-"):
                        return resulto - resultB1
                    else:
                        return None

                else:

                    resultC1 = 0
                    
                    if (operator2 == "+" or operator2 == "-"):
                        
                        if (operator2 == "+"):
                            resultC1 = resulto + rightnumber2
                        elif (operator2 == "-"):
                            resultC1 = resulto - rightnumber2
                        else:
                            return None

                        if (operator3 == "+"):
                            return resultC1 + rightnumber3
                        elif (operator3 == "-"):
                            return resultC1 - rightnumber3
                        else:
                            return None

                    else:
                        return None

        else:
            
            if (operator2 == "*" or operator2 == "/"):
                
                if (operator2 == "*"):
                    resulto = leftnumber2 * rightnumber2
                elif (operator2 == "/"):
                    resulto = leftnumber2 / rightnumber2
                else:
                    return None

                if (operator3 == "*" or operator3 == "/"):
                    
                    resultA2 = 0

                    if (operator3 == "*"):
                        resultA2 = resulto * rightnumber3
                    elif (operator3 == "/"):
                        resultA2 = resulto / rightnumber3
                    else:
                        return None

                    if (operator1 == "+"):
                        return leftnumber1 + resultA2
                    elif (operator1 == "-"):
                        return leftnumber1 - resultA2
                    else:
                        return None

                else:

                    if (operator1 == "+" or operator1 == "-"):

                        resultB2 = 0

                        if (operator1 == "+"):
                            resultB2 = leftnumber1 + resulto
                        elif (operator1 == "-"):
                            resultB2 = leftnumber1 - resulto
                        else:
                            return None

                        if (operator3 == "+"):
                            return resultB2 + rightnumber3
                        elif (operator3 == "-"):
                            return resultB2 - rightnumber3
                        else:
                            return None

                    else:
                        return None

            else:

                if (operator3 == "*" or operator3 == "/"):

                    if (operator3 == "*"):
                        resulto = leftnumber3 * rightnumber3
                    elif (operator3 == "/"):
                        resulto = leftnumber3 / rightnumber3
                    else:
                        return None

                    if (operator1 == "+" or operator1 == "-"):

                        resultA3 = 0
                        
                        if (operator1 == "+"):
                            resultA3 = leftnumber1 + rightnumber1
                        elif (operator1 == "-"):
                            resultA3 = leftnumber1 - rightnumber1
                        else:
                            return None

                        if (operator2 == "+" or operator2 == "-"):
                            
                            if (operator2 == "+"):
                                return resultA3 + resulto
                            elif (operator2 == "-"):
                                return resultA3 - resulto
                            else:
                                return None

                    else:
                        return None
                    
                else:

                    if (operator1 == "+" or operator1 == "-"):
                        
                        if (operator1 == "+"):
                            resulto = leftnumber1 + rightnumber1
                        elif (operator1 == "-"):
                            resulto = leftnumber1 - rightnumber1
                        else:
                            return None

                        resultA4 = 0

                        if (operator2 == "+" or operator2 == "-"):

                            if (operator2 == "+"):
                                resultA4 = resulto + rightnumber2
                            elif (operator2 == "-"):
                                resultA4 = resulto - rightnumber2
                            else:
                                return None

                            if (operator3 == "+" or operator3 == "-"):

                                if (operator3 == "+"):
                                    return resultA4 + rightnumber3
                                elif (operator3 == "-"):
                                    return resultA4 - rightnumber3
                            else:
                                return None

                        else:
                            return None

                    else:
                        return None
