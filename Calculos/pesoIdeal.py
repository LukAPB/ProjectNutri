import os
import math

# Peso ideal:
#  mulher 
# 21× h²
#  Homem 
# 23×h²
#  Idoso: 
# 24,5 ×h²
# Peso máximo 
# 25× h²

def pesoI(sexo, altura, idade):
    if idade == 0 or altura == 0:
        pesoIdeal = "Peso Ideal não calculado"
    else:
        if sexo == 'M' or sexo == 'm':
            if idade > 17 and idade < 62:
                pesoIdeal = 23 * (altura ** 2)
            elif idade >= 62:
                pesoIdeal = 24.5 * (altura ** 2)
        elif sexo == 'F' or sexo == 'f':
            if idade > 17 and idade < 62:
                pesoIdeal = 21 * (altura ** 2)
            elif idade >= 62:
                pesoIdeal = 24.5 * (altura ** 2)
        else:
            pesoIdeal = "Sexo inválido"
    
    return pesoIdeal



