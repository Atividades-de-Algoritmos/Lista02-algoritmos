
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# Faça um algoritmo que leia três valores e descubra qual o menor valor.

# entrada de dados
valor1 = int(input("informe o valor 1: "))
valor2 = int(input("informe o valor 2: "))
valor3 = int(input("informe o valor 3: "))

# processamento e saida de dados
if (valor1 < valor2 and valor1 < valor3): # se o valor 1 for menor que o valor 2 e o valor 1 for menor que o valor 3
  print(f"{valor1} é o menor")
elif (valor2 < valor1 and valor2 < valor3): # se o valor 2 for menor que o valor 1 e o valor 2 for menor que o valor 3
  print(f"{valor2} é o menor")
elif (valor3 < valor1 and valor3 < valor2): # se o valor 3 for menor que o valor 1 e o valor 3 for menor que o valor 2
  print(f"{valor3} é o menor")
else: # se nenhum dos valores for menor que o outro, forem iguais
  print("Nenhum dos valores é menor, são iguais")

print("Fim do programa")
