import os


class Calpercentil():

    def CbPercentil(cb,idade,sexo):
        if idade >= 18 and idade <25:
            if sexo == 'm' or sexo == 'M':
                cbperc = 30.7
            else:
                cbperc = 26.8
        elif idade >= 25 and idade < 30:
            if sexo == 'm' or sexo == 'M':
                cbperc = 31.8
            else:
                cbperc = 27.6
        elif idade >= 30 and idade < 35:
            if sexo == 'm' or sexo == 'M':
                cbperc = 32.5
            else:
                cbperc = 28.6
        elif idade >= 35 and idade < 40:
            if sexo == 'm' or sexo == 'M':
                cbperc = 32.9
            else:
                cbperc = 29.4
        elif idade >= 40 and idade < 45:
            if sexo == 'm' or sexo == 'M':
                cbperc = 32.8
            else:
                cbperc = 29.7
        elif idade >= 45 and idade < 50:
            if sexo == 'm' or sexo == 'M':
                cbperc = 32.6
            else:
                cbperc = 30.1
        elif idade >= 50 and idade < 55:
            if sexo == 'm' or sexo == 'M':
                cbperc = 32.3
            else:
                cbperc = 30.6
        elif idade >= 55 and idade < 60:
            if sexo == 'm' or sexo == 'M':
                cbperc = 32.3
            else:
                cbperc = 30.9
        elif idade >= 60 and idade < 65:
            if sexo == 'm' or sexo == 'M':
                cbperc = 32.0
            else:
                cbperc = 30.8
        elif idade >= 65 and idade < 70:
            if sexo == 'm' or sexo == 'M':
                cbperc = 31.1
            else:
                cbperc = 30.5
        elif idade >= 70 and idade < 75:
            if sexo == 'm' or sexo == 'M':
                cbperc = 30.7
            else:
                cbperc = 30.3
        elif idade >= 75 and idade < 80:
            if sexo == 'm' or sexo == 'M':
                cbperc = 24.5
            else:
                cbperc = 24.9
        elif idade >= 80 and idade < 85:
            if sexo == 'm' or sexo == 'M':
                cbperc = 23.7
            else:
                cbperc = 23.5
        else:
            if sexo == 'm' or sexo == 'M':
                cbperc = 23.0
            else:
                cbperc = 22.1
        adeqCB = cb*100 / cbperc
        return(adeqCB)

    def NameAdq (adq):
        if adq == 0:
            nomecl = ("CB Não Calculado")
        elif adq > 120:
            nomecl = (" Obesidade")
        elif adq >=110 and adq <120:
            nomecl = ("Sobrepeso")
        elif adq >=90 and adq < 110:
            nomecl = (" Eutrofia")
        elif adq >=80 and adq < 90:
            nomecl = (" Depleção Discreta")
        elif adq >=60 and adq < 80:
            nomecl = (" Depleção Moderada")
        else:
            nomecl = (" Depleção Grave")
        return(nomecl) 

    
        
    