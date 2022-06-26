
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# Faça um algoritmo que leia três valores e descubra qual o maior valor.

# entrada de dados
valor1 = int(input("informe o valor 1: "))
valor2 = int(input("informe o valor 2: "))
valor3 = int(input("informe o valor 3: "))

# processamento e saida de dados
if (valor1 > valor2 and valor1 > valor3): # se o valor 1 for maior que o valor 2 e o valor 1 for maior que o valor 3
  print(f"{valor1} é o maior")
elif (valor2 > valor1 and valor2 > valor3): # se o valor 2 for maior que o valor 1 e o valor 2 for maior que o valor 3
  print(f"{valor2} é o maior")
elif (valor3 > valor1 and valor3 > valor2): # se o valor 3 for maior que o valor 1 e o valor 3 for maior que o valor 2
  print(f"{valor3} é o maior")
else: # se nenhum dos valores for maior que o outro
  print("Nenhum dos valores é maior, são iguais")

  print("Fim do programa")
  
