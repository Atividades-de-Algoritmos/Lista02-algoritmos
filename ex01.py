#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 1. Faça um algoritmo que leia três valores e descubra qual 
# o maior valor.                                             

# Entrada de dados

valor1 = int(input("informe o valor 1: ")) # Solicita o primeiro valor
valor2 = int(input("informe o valor 2: ")) # Solicita o segundo valor
valor3 = int(input("informe o valor 3: ")) # Solicita o terceiro valor

# Processamento e saída de dados

if (valor1 > valor2 and valor1 > valor3): # Se valor1 for maior que valor2 e valor1 for maior que valor3
  print(f"{valor1} é o maior valor") # Imprime a mensagem informando que valor1 é maior

elif (valor2 > valor1 and valor2 > valor3): # Se valor2 for maior que valor1 e valor2 for maior que valor3
  print(f"{valor2} é o maior valor") # Imprime a mensagem informando que valor2 é maior

elif (valor3 > valor1 and valor3 > valor2): # Se valor3 for maior que valor1 e valor3 for maior que valor2
  print(f"{valor3} é o maior valor") # Imprime a mensagem informando que valor3 é maior

else: # Se nenhum dos valores for maior que o outro
  print("Nenhum dos valores é maior, são iguais") # Imprime a mensagem informando que os valores são iguais

print("fim do programa") # Informa ao usuário que o programa terminou
