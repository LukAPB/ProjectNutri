

def calpe(aj,cb,sexo,etnia,idade):
    if aj == 0:
            return("Peso não calculada")
    else:
            if etnia == 'B':
                if sexo == 'F':
                    if idade > 18 and idade <60:
                        ajT = aj * 1.01 
                        cbT = cb* 2.81
                        totalf = (ajT + cbT) - 66.04
                        return (totalf)
                    elif idade > 59 and idade <81:
                        ajT = aj * 1.09 
                        cbT = cb* 2.68
                        totalf = (ajT + cbT) - 65.51
                        return (totalf)
                else:
                    if idade > 18 and idade <60:
                        ajT = aj * 1.19 
                        cbT = cb * 3.14
                        totalf = (ajT + cbT) - 86.82
                        return (totalf)
                    elif idade > 59 and idade <81:
                        ajT = aj * 1.10 
                        cbT = cb* 3.07
                        totalf = (ajT + cbT) - 75.81
                        return (totalf)
            else:
                if sexo == 'F':
                    if idade > 18 and idade <60:
                        ajT = aj * 1.24 
                        cbT = cb* 2.97
                        totalf = (ajT + cbT) - 82.48
                        return (totalf)
                    elif idade > 59 and idade <81:
                        ajT = aj * 1.50 
                        cbT = cb * 2.58
                        totalf = (ajT + cbT) - 84.22
                        return (totalf)
                else:
                    if idade > 18 and idade <60:
                        ajT = aj * 1.09 
                        cbT = cb * 3.14
                        totalf = (ajT + cbT) - 83.72
                        return (totalf)
                    elif idade > 59 and idade <81:
                        ajT = aj * 0.44 
                        cbT = cb* 2.86
                        totalf = (ajT + cbT) - 39.21
                        return (totalf)
