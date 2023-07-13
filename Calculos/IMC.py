import os


def imcV (idade,altura,peso):   
   if idade < 18:
      return 'Calculo IMC indisponivél'
   else:
      valor = peso/ altura **2
   return valor



def imc (idade,altura,peso):

   valor = imcV(idade,altura,peso)
   if idade < 18:
      'Calculo indisponivél'
   elif idade >=18 and idade<61:
      if valor < 16:
         return  'Desnutrição Grau III ou Desnutrição Grave'
      elif valor >= 16 and valor < 17:
            return  'Desnutrição Grau II ou Desnutrição Moderada'
      elif valor >= 17 and valor < 18.5:
         return  'Desnutrição Grau I ou Desnutrição Leve'
      elif valor >= 18.5 and valor < 25 :
         return  'Normal ou Eutrófico ou Etrofia'
      elif valor >= 25 and valor < 30 :
         return  'Sobrepesso ou Excesso de Peso'
      elif valor >= 30 and valor < 35 :
         return  'Obesidade Leve ou Obesidade Grau I'
      elif valor >= 35 and valor < 40 :
         return  'Obesidade Moderada ou Obesidade Grau II'
      else:
         return  'Obesidade Grave ou Obesidade Grau III'           
   else:
      if valor < 22:
         return  'Magreza'
      elif valor >= 22 and valor <28:
         return 'Eutrofia'
      else:
         return  'Excesso de Peso'
            
   return "Sem Classificação"

   