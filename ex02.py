#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 2. Faça um algoritmo que leia três valores e descubra qual 
# o menor valor.                                             

# entrada de dados
valor1 = int(input("informe o valor 1: ")) # Solicita o primeiro valor
valor2 = int(input("informe o valor 2: ")) # Solicita o segundo valor
valor3 = int(input("informe o valor 3: ")) # Solicita o terceiro valor

# processamento e saída de dados
if (valor1 < valor2 and valor1 < valor3): # se o valor 1 for menor que o valor 2 e o valor 1 for menor que o valor 3
  print(f"{valor1} é o menor") # imprime a mensagem se o valor 1 for menor
elif (valor2 < valor1 and valor2 < valor3): # se o valor 2 for menor que o valor 1 e o valor 2 for menor que o valor 3
  print(f"{valor2} é o menor") # imprime a mensagem se o valor 2 for menor
elif (valor3 < valor1 and valor3 < valor2): # se o valor 3 for menor que o valor 1 e o valor 3 for menor que o valor 2
  print(f"{valor3} é o menor") # imprime a mensagem se o valor 3 for menor
else: # se nenhum dos valores for menor que o outro, forem iguais
  print("Nenhum dos valores é menor, são iguais") # imprime a mensagem se nenhum dos valores for menor que o outro

print("fim do programa") # Informa ao usuário que o programa terminou
