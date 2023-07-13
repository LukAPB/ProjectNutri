import os


class DCTCalpercentil():
   

    def DCTPercentil(dct, idade, sexo):
        sexo = sexo.lower()

        percentis = {
            (18, 25): {'m': 10.0, 'f': 18.5},
            (25, 30): {'m': 11.0, 'f': 20.0},
            (30, 35): {'m': 12.0, 'f': 22.5},
            (35, 40): {'m': 12.0, 'f': 23.5},
            (40, 45): {'m': 12.0, 'f': 24.5},
            (45, 50): {'m': 12.0, 'f': 25.5},
            (50, 55): {'m': 11.5, 'f': 25.5},
            (55, 60): {'m': 11.5, 'f': 26.0},
            (60, 65): {'m': 11.5, 'f': 26.0},
            (65, 70): {'m': 11.0, 'f': 25.0},
            (70, 75): {'m': 11.0, 'f': 24.0},
            (75, 80): {'m': 7.0, 'f': 14.6},
            (80, 85): {'m': 6.6, 'f': 12.7},
        }

        for range_age, percentil in percentis.items():
            if idade >= range_age[0] and idade < range_age[1]:
                return dct * 100 / percentil[sexo]

        if sexo == 'm':
            return dct * 100 / 6.5
        else:
            return dct * 100 / 11.5

    def NameAdq (adq):
        if adq == 0:
            nomecl = ("DCT Não Calculado")
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

    
        
    